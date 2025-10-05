from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session
from app.models.user_model import NewUser
from app.schemas.user_schemas import UserSchema
from app.schemas.todo_schemas import TaskSchema
from app.models.todo_model import NewTask


async def create_user(user : NewUser):
    async with async_session() as session:
        db_user = NewUser(**user.dict())
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user.user_id
    users = result.scalars().all()
    if users(len) == 3:
        raise HTTPException(status_code=401, detail="Fatal error\nUser cannot be created")
    
async def show_users():
    async with async_session() as session:
        result = await session.execute(select(NewUser))
        users = result.scalars().all()
        return users
    
async def update_user_info(user_id: int, user: UserSchema):
    async with async_session() as session:
        db_user = await session.get(NewUser, user_id)
        if not db_user:
            return False
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        await session.commit()
        await session.refresh(db_user)
        return db_user
    
async def delete_user(task_id: int):
    async with async_session() as session:
       db_user = await session.get(NewUser, task_id)
       if not db_user:
           return False
       await session.delete(db_user)
       await session.commit()
       return True 