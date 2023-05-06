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
    return {"message": "Hello, World!"}
