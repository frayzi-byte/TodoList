from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session
from app.models.user_model import NewUser
from app.schemas.user_schemas import UserSchema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    if len(password) > 72:
        password = password[:72]
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

from app.schemas.user_schemas import UserCreate  # muda aqui

async def create_user(user: UserCreate):
    async with async_session() as session:
        hashed_pw = hash_password(user.password)
        db_user = NewUser(
            name=user.name,
            email=user.email,
            password=hashed_pw
        )
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user

    async with async_session() as session:
        hashed_pw = hash_password(user.password)
        db_user = NewUser(
            name=user.name,
            email=user.email,
            password=hashed_pw
        )
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user

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
            if key == "password" and value:
                value = hash_password(value)
            setattr(db_user, key, value)
        await session.commit()
        await session.refresh(db_user)
        return db_user

async def delete_user(user_id: int):
    async with async_session() as session:
        db_user = await session.get(NewUser, user_id)
        if not db_user:
            return False
        await session.delete(db_user)
        await session.commit()
        return True

async def get_user_by_email(email: str):
    async with async_session() as session:
        result = await session.execute(select(NewUser).where(NewUser.email == email))
        return result.scalars().first()
