from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
import os



db_url = os.getenv("DATABASE_URL")

engine = create_async_engine(db_url, echo = True)


AsyncSessionLocal = async_sessionmaker(bind = engine, class_ = AsyncSession, expire_on_commit = False)


class Base(DeclarativeBase):
    pass

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session