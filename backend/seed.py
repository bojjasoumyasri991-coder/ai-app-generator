from backend.database import SessionLocal
from backend import db_models as models

db = SessionLocal()

user = models.User(
    email="admin@gmail.com",
    password="admin123",
    role="admin"
)

db.add(user)
db.commit()

print("✅ User created successfully!")