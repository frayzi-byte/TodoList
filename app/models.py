from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    password: str

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
