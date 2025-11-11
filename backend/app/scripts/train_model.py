# backend/scripts/train_model.py
import pandas as pd
import joblib
import os
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

DATA_PATH = os.getenv("DATA_PATH", "./backend/data/creditcard.csv")
MODEL_PATH = os.getenv("MODEL_PATH", "../app/model.joblib")  # when executed from scripts/ folder

def train_and_save():
    df = pd.read_csv(DATA_PATH)
    # Keep a few features: Time, Amount, PCA features if present V1..V28
    feature_cols = []
    if "Time" in df.columns:
        feature_cols.append("Time")
    if "Amount" in df.columns:
        feature_cols.append("Amount")
    pca_cols = [c for c in df.columns if c.startswith("V")]
    feature_cols += pca_cols[:8]  # use first 8 PCA features for simplicity
    X = df[feature_cols].fillna(0)
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)

    model = IsolationForest(n_estimators=200, contamination=0.003, random_state=42, behaviour="new")
    model.fit(Xs)

    # save scaler+model together
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump({"model": model, "scaler": scaler, "feature_cols": feature_cols}, MODEL_PATH)
    print("Saved model to", MODEL_PATH)

if __name__ == "__main__":
    train_and_save()
