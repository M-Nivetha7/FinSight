# backend/app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, crud, db, auth, ml_model
from .db import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FinSight API")

origins = ["http://localhost:3000", "http://localhost:5173"]  # frontend dev ports
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db_ = SessionLocal()
    try:
        yield db_
    finally:
        db_.close()

model = ml_model.load_model()

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = auth.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    u = crud.create_user(db, user.username, user.password)
    return u

@app.post("/transactions/", response_model=schemas.TransactionOut)
def ingest_transaction(tx: schemas.TransactionIn, db: Session = Depends(get_db)):
    # predict risk
    res = ml_model.predict_risk(model, tx.dict())
    created = crud.create_transaction(db, tx, predicted_fraud=res["predicted_fraud"], risk_score=res["risk_score"])
    return created

@app.get("/transactions/", response_model=list[schemas.TransactionOut])
def list_transactions(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.get_transactions(db, skip, limit)

@app.get("/health")
def health():
    return {"status": "ok"}
