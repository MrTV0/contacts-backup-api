from sqlalchemy.orm import Session

import models
import schemas
import auth


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(full_name=user.full_name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.full_name == name).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def del_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id==user_id).delete()
    db.query(models.Contact).filter(models.Contact.users_id==user_id).delete()
    db.query(models.Number).filter(models.Number.users_id==user_id).delete()
    db.commit()




def create_contact(db: Session, contact: schemas.ContactCreate, user_id: int):
    db_contact = models.Contact(**contact.dict(), users_id=user_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_name_contact_by_user(db: Session, name: str, user: int):
    return db.query(models.Contact).filter(models.Contact.full_name == name).first() and db.query(models.Contact).filter(models.Contact.users_id == user).first()

def get_email_contact_by_user(db: Session, email: str, user: int):
    if email != "":
        output = db.query(models.Contact).filter(models.Contact.email == email).first()
    else:
        output = False
    return output and db.query(models.Contact).filter(models.Contact.users_id == user).first()

def get_contacts(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Contact).offset(skip).limit(limit).all()





def create_number(db: Session, number: schemas.NumberCreate, user_id: int, contact_id: int):
    db_number = models.Number(**number.dict(), users_id=user_id, contacts_id=contact_id)
    db.add(db_number)
    db.commit()
    db.refresh(db_number)
    return db_number

def get_number_by_contact(db: Session, number: str, contact: int):
    return db.query(models.Number).filter(models.Number.phonenumber == number).first() and db.query(models.Number).filter(models.Number.contacts_id == contact).first()

def get_number(db: Session, number_id: int):
    return db.query(models.Number).filter(models.Number.id == number_id).first()

def get_number_by_user(db: Session, user_id: int, contact_id: int):
    return db.query(models.Number).filter(models.Number.users_id == user_id).first() and db.query(models.Number).filter(models.Number.contacts_id == contact_id).first()

def get_numbers(db: Session, contact_id: int):
    return db.query(models.Number).filter(models.Number.contacts_id == contact_id).all()

def update_number(db: Session, number_id: int, number: schemas.NumberUpdate):
    db.query(models.Number).filter(models.Number.id == number_id).update(vars(number))
    db.commit()
    return db.query(models.Number).filter(models.Number.id == number_id).first()
