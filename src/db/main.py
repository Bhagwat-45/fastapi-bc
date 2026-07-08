from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config

engine = create_async_engine(url=Config.DATABASE_URL, echo=True)

async def init_db():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT current_database(), version();"))
        print(result.all())

