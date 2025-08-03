from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/todo_db", echo=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async def ping_db():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Connected PostgreSQL successfully!")
    except Exception as e:
        print("❌ Error connecting to PostgreSQL:", e)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)