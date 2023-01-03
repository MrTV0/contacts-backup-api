from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    contacts = relationship("Contact", back_populates="user")


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, index=True)
    users_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="contacts")
    numbers = relationship("Number", back_populates="phone")


class Number(Base):
    __tablename__ = "phonenumbers"

    id = Column(Integer, primary_key=True, index=True)
    phonenumber = Column(String, index=True)
    relation = Column(String, index=True)
    contacts_id = Column(Integer, ForeignKey("contacts.id"))
    users_id = Column(Integer, ForeignKey("users.id"))

    phone = relationship("Contact", back_populates="numbers")
