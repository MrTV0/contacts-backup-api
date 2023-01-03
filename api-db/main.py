from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user_name = crud.get_user_by_name(db, name=user.full_name)
    if db_user_name:
        raise HTTPException(status_code=400, detail="Name already registered")
    db_user_email = crud.get_user_by_email(db, email=user.email)
    if db_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.del_user(db, user_id=user_id)
    return {"delete": "Successful"}





@app.post("/user/{user_id}/contact/", response_model=schemas.Contact)
def create_contact_for_user(user_id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact_name = crud.get_name_contact_by_user(db, name=contact.full_name, user=user_id)
    if db_contact_name:
        raise HTTPException(status_code=400, detail="Contact already registered")
    db_contact_email = crud.get_email_contact_by_user(db, email=contact.email, user=user_id)
    if db_contact_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_contact(db=db, contact=contact, user_id=user_id)


@app.get("/contacts/", response_model=list[schemas.Contact])
def read_contacts(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    contacts = crud.get_contacts(db, skip=skip, limit=limit)
    return contacts






@app.post("/user/{user_id}/contact/{contact_id}", response_model=schemas.Number)
def create_number_for_contact(user_id: int, contact_id: int, number: schemas.NumberCreate, db: Session = Depends(get_db)):
    db_number = crud.get_number_by_contact(db, number=number.phonenumber, contact=contact_id)
    if db_number:
        raise HTTPException(status_code=400, detail="Number already registered")
    return crud.create_number(db=db, number=number, user_id=user_id, contact_id=contact_id)


@app.get("/numbers/", response_model=list[schemas.Number])
def read_numbers(user: int, contact: int, db: Session = Depends(get_db)):
    number = crud.get_number_by_user(db, user_id=user, contact_id=contact)
    if number is None:
        raise HTTPException(status_code=404, detail="Number not found")
    numbers = crud.get_numbers(db, contact_id=contact)
    return numbers


@app.put("/number/{number_id}", response_model=schemas.Number)
def update_number(number_id: int, number: schemas.NumberUpdate, db: Session = Depends(get_db)):
    db_number = crud.get_number(db, number_id=number_id)
    if db_number is None:
        raise HTTPException(status_code=400, detail="Number doesn't exist")
    return crud.update_number(db, number_id=number_id, number=number)