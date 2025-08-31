from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db import Base
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

class NewUser(Base):
    __tablename__ = "tasks"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    user_email = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())