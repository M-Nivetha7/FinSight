# backend/app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash, verify_password

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str, password: str, is_admin: bool=False):
    user = models.User(username=username, hashed_password=get_password_hash(password), is_admin=is_admin)
    db.add(user); db.commit(); db.refresh(user)
    return user

def create_transaction(db: Session, tx_in: schemas.TransactionIn, predicted_fraud=None, risk_score=None):
    tx = models.Transaction(
        transaction_id=tx_in.transaction_id,
        customer_id=tx_in.customer_id,
        amount=tx_in.amount,
        location=tx_in.location,
        card_type=tx_in.card_type,
        predicted_fraud=predicted_fraud,
        risk_score=risk_score
    )
    db.add(tx); db.commit(); db.refresh(tx)
    return tx

def get_transactions(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()
