from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

class NewUser(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    user_email = Column(String, nullable=False)