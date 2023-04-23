from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.folder import Folder


class FolderController:
    async def get_folder(session: AsyncSession, uuid: str):
        if uuid is None:
            stmt = select(Folder).where((Folder.deleted_at.is_(None)))
            result = await session.execute(stmt)
            folders = result.scalars().all()
            return folders
        else:
            stmt = select(Folder).where(
                (Folder.deleted_at.is_(None)) & (Folder.uuid == uuid)
            )
            result = await session.execute(stmt)
            folders = result.scalars().all()
            return folders

    async def make_folder(session: AsyncSession, name: str):
        async with session.begin():
            folder = Folder(name=name)
            session.add(folder)
            await session.flush()
            return folder

    async def update_folder(session: AsyncSession, uuid: str, name: str):
        async with session.begin():
            folder = await session.get(Folder, uuid)
            if folder:
                folder.name = name
                await session.flush()
                return folder
            else:
                return None

    async def delete_folder(session: AsyncSession, uuid: str):
        stmt = (
            update(Folder).where(Folder.uuid == uuid).values(deleted_at=datetime.now())
        )
        await session.execute(stmt)
        await session.commit()
