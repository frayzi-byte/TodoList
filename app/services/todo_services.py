from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session
from app.models.todo_model import NewTask
from app.schemas.todo_schemas import TaskSchema

async def create_task(task : NewTask):
    async with async_session() as session:
        db_task = NewTask(**task.dict())
        session.add(db_task)
        await session.commit()
        await session.refresh(db_task)
        return db_task.id
    
async def list_tasks():
    async with async_session() as session:
        result = await session.execute(select(NewTask))
        tasks = result.scalars().all()
        return tasks
    
async def update_task(task_id: int, task: TaskSchema):
    async with async_session() as session:
        db_task = await session.get(NewTask, task_id)
        if not db_task:
            return False
        for key, value in task.dict().items():
            setattr(db_task, key, value)
        await session.commit()
        return True
    
async def delete_task(task_id: int):
    async with async_session() as session:
       db_task = await session.get(NewTask, task_id)
       if not db_task:
           return False
       await session.delete(db_task)
       await session.commit()
       return True 