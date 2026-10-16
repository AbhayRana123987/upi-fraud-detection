from fastapi import FastAPI
from pathlib import Path
import joblib

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "random_forest_candidate.pkl")
preprocessor = joblib.load(BASE_DIR / "models" / "preprocessor.pkl")

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







from pydantic import BaseModel


class TransactionInput(BaseModel):
    transaction_type: str
    merchant_category: str
    amount: float
    sender_age_group: str
    receiver_age_group: str
    sender_state: str
    sender_bank: str
    receiver_bank: str
    device_type: str
    network_type: str
    hour_of_day: int
    day_of_week: str
    is_weekend: int


@app.post("/predict")
def predict_fraud(transaction: TransactionInput):
    import pandas as pd

    input_data = pd.DataFrame([{
        "transaction type": transaction.transaction_type,
        "merchant_category": transaction.merchant_category,
        "amount (INR)": transaction.amount,
        "sender_age_group": transaction.sender_age_group,
        "receiver_age_group": transaction.receiver_age_group,
        "sender_state": transaction.sender_state,
        "sender_bank": transaction.sender_bank,
        "receiver_bank": transaction.receiver_bank,
        "device_type": transaction.device_type,
        "network_type": transaction.network_type,
        "hour_of_day": transaction.hour_of_day,
        "day_of_week": transaction.day_of_week,
        "is_weekend": transaction.is_weekend
    }])

    processed_data = preprocessor.transform(input_data)
    prediction = int(model.predict(processed_data)[0])

    prediction = int(model.predict(processed_data)[0])

    print("Model classes:", model.classes_)
    print("Predicted class:", prediction)   

    print("Model classes:", model.classes_)
    print("Predicted class:", prediction)
    print("Probabilities:", model.predict_proba(processed_data)[0])

    probability = None
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(processed_data)[0][1])

    return {
        "prediction": "Fraudulent" if prediction == 1 else "Genuine",
        "fraud_probability": probability
    }


