from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

class NewTask(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_done = Column(Boolean, nullable=False)
