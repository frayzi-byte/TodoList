from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_name: str
    user_email: str

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    user_name: str
    user_email: str
