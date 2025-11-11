# backend/app/ml_model.py
import joblib
import os
import numpy as np
import pandas as pd

MODEL_PATH = os.getenv("MODEL_PATH", "./backend/app/model.joblib")

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def predict_risk(model, tx_record: dict):
    """
    tx_record: dict with keys amount, optionally other features.
    For IsolationForest we expect a numeric feature array.
    """
    if model is None:
        return {"predicted_fraud": False, "risk_score": 0.0}

    # Compose feature vector — adjust according to model training
    # Here we just use amount (scaled) as simple example:
    features = np.array([[tx_record.get("amount", 0.0)]])
    pred = model.predict(features)  # for IsolationForest: -1 anomaly, 1 normal
    score = model.decision_function(features)[0]
    predicted_fraud = True if pred[0] == -1 else False
    # convert score to 0..1 risk (higher => riskier)
    risk_score = float(np.tanh(-score))  # crude transform
    return {"predicted_fraud": predicted_fraud, "risk_score": risk_score}
