from typing import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.app.core.config import settings
from backend.app.core.logging import logger

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=True,
    future=True,
)

async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Exception occurred when getting the session: {e}")
            await session.rollback()
            raise e
        finally:
            await session.close()


async def init_db() -> None:
    async with engine.begin() as conn:
        logger.info("Database connection test")
        result = await conn.execute(text("select 'it works'; "))
        logger.info(result.all())


async def dispose_db():
    await engine.dispose()
