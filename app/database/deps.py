from typing import Generator
from .session import async_session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_async_session() -> Generator[AsyncSession, None, None]:
    async with async_session() as session:
        yield session
