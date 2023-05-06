# import modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

# Creating a FastAPI instance.
app = FastAPI()

# Creating an instance of the `CORSMiddleware` class.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the models
NB_pickle = pickle.load(open('NB_pickle.pkl', 'rb'))
LOG_pickle = pickle.load(open('LOG_pickle.pkl', 'rb'))
KNN_pickle = pickle.load(open('KNN_pickle.pkl', 'rb'))
SVM_pickle = pickle.load(open('SVM_pickle.pkl', 'rb'))
XGB_pickle = pickle.load(open('XGB_pickle.pkl', 'rb'))

# API routes.


@app.get("/")
def index():
    return {"message": "Casper Maringe, Thesis Backend Service"}


@app.post('/v1/api/predict')
async def predict(data: dict):
    try:
        encripted_agent_account = data['data']['encripted_agent_account']
        city = data['data']['city']
        association = data['data']['association']
        agent_name = data['data']['agent_name']
        encripted_billid = data['data']['encripted_billid']
        payment_channels = data['data']['payment_channels']
        standardised_amount = data['data']['standardised_amount']
        previous_transaction_count = data['data']['previous_transaction_count']

        makePredictionsData = [encripted_agent_account, city, association, agent_name, encripted_billid,
                               payment_channels, standardised_amount, previous_transaction_count]

        try:
            prediction = []
            # Make prediction using model loaded from disk as per the data.
            if data['algorithim'] == 'NB':
                prediction = NB_pickle.predict([makePredictionsData])
            elif data['algorithim'] == 'LOG':
                prediction = LOG_pickle.predict([makePredictionsData])
            elif data['algorithim'] == 'KNN':
                prediction = KNN_pickle.predict([makePredictionsData])
            elif data['algorithim'] == 'SVM':
                prediction = SVM_pickle.predict([makePredictionsData])
            elif data['algorithim'] == 'XGB':
                prediction = XGB_pickle.predict([makePredictionsData])
            else:
                return {"error": "missing valid algorithim", "status": 400}

            # Take the first value of prediction
            print(prediction)
            output = prediction[0]
            if output == 1:
                return {"is_fraud": True, "status": 200}
            else:
                return {"is_fraud": False, "status": 200}
        except Exception as e:
            return {'error': str(e), "status": 500}
    except Exception as e:
        return {'error': str(e), "status": 500}
