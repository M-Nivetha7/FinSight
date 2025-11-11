# backend/app/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    customer_id = Column(String, index=True)
    amount = Column(Float)
    time = Column(DateTime, server_default=func.now())
    location = Column(String, nullable=True)
    card_type = Column(String, nullable=True)
    predicted_fraud = Column(Boolean, nullable=True)
    risk_score = Column(Float, nullable=True)
