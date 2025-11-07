from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


async def ping_db():
    """Verifica a conexão com o banco"""
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Connected PostgreSQL successfully!")
    except Exception as e:
        print("❌ Error connecting to PostgreSQL:", e)


async def init_db():
    """Cria as tabelas do banco se não existirem"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("📦 Tables created successfully!")

async def list_tables():
    async with engine.begin() as conn:
        result = await conn.execute(text(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
        ))
        tables = [row[0] for row in result]
        print("📋 Tabelas no banco:", tables)
