from pydantic import BaseModel


class UserSchema(BaseModel):
    user_name: str
    user_email: str