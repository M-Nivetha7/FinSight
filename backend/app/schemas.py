# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    is_admin: bool
    class Config:
        orm_mode = True

class TransactionIn(BaseModel):
    transaction_id: str
    customer_id: str
    amount: float
    location: Optional[str] = None
    card_type: Optional[str] = None
    time: Optional[datetime] = None

class TransactionOut(TransactionIn):
    id: int
    predicted_fraud: Optional[bool]
    risk_score: Optional[float]
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
