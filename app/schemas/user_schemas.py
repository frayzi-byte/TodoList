from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
