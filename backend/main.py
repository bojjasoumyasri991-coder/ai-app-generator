from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import SessionLocal, engine
from backend import db_models as models

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔐 LOGIN
@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == email,
        models.User.password == password
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "email": user.email,
        "role": user.role
    }


# ➕ ADD CONTACT
@app.post("/contacts")
def add_contact(name: str, email: str, user_id: int, db: Session = Depends(get_db)):
    contact = models.Contact(name=name, email=email, user_id=user_id)
    db.add(contact)
    db.commit()
    db.refresh(contact)

    return {
        "message": "Contact added",
        "contact_id": contact.id
    }


# 📄 GET CONTACTS
@app.get("/contacts")
def get_contacts(user_id: int, db: Session = Depends(get_db)):
    contacts = db.query(models.Contact).filter(
        models.Contact.user_id == user_id
    ).all()

    return contacts