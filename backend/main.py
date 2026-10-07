from fastapi import FastAPI
import joblib

app = FastAPI(
    title="UPI Fraud Detection API",
    description="API for detecting potentially fraudulent UPI transactions",
    version="1.0.0"
)

# Load trained model and preprocessor
model = joblib.load("../models/random_forest_candidate.pkl")
preprocessor = joblib.load("../models/preprocessor.pkl")


@app.get("/")
def home():
    return {
        "message": "UPI Fraud Detection API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }