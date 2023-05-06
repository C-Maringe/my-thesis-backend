# In `main.py`, import FastAPI.
from fastapi import FastAPI

# Create a FastAPI instance.
app = FastAPI()

# Define your API routes.
@app.get("/")
def index():
    return {"message": "Hello, World!"}

# Run your FastAPI server.
# uvicorn main:app --reload