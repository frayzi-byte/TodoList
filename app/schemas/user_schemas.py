from pydantic import BaseModel, DateTime
from sqlalchemy import ForeignKey


class UserSchema(BaseModel):
    user_id = int
    user_name = str
    user_email = str
    created_at = DateTime(timezone=True)