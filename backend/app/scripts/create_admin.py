from app.db import SessionLocal
from app import crud
db = SessionLocal()
crud.create_user(db, "admin", "admin123", is_admin=True)
print("Admin created")
