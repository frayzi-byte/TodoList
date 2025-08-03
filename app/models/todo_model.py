from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class NewTask(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    compl = Column(Boolean, nullable=False)