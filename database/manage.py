from sqlalchemy.ext.asyncio import AsyncSession

from database.base import engine, base, async_session


async def init_models():
    async with engine.begin() as connection:
        await connection.run_sync(base.metadata.drop_all)
        await connection.run_sync(base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
