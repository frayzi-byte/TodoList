from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session
from app.models.project_model import NewProject
from app.schemas.project_schemas import ProjectSchema

async def create_project(project : NewProject):
    async with async_session() as session:
        db_project = NewProject(**project.dict())
        session.add(db_project)
        await session.commit()
        await session.refresh(db_project)
        return db_project.id