from pydantic import BaseModel


class NumberUpdate(BaseModel):
    phonenumber: str
    relation: str


class NumberBase(BaseModel):
    phonenumber: str
    relation: str


class NumberCreate(NumberBase):
    pass


class Number(NumberBase):
    id: int
    contacts_id: int
    users_id: int

    class Config:
        orm_mode = True


class ContactBase(BaseModel):
    full_name: str
    email: str | None = None


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    users_id: int
    numbers: list[Number] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    full_name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    contacts: list[Contact] = []

    class Config:
        orm_mode = True