from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

class NewProject(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    project_desc = Column(String, nullable=False)