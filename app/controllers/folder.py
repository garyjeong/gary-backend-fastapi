from datetime import datetime
from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.folder import Folder
from app.schemas.folder import FolderResponse


class FolderController:
    async def get_folder(
        session: AsyncSession, folder_uid: str = None
    ) -> list[FolderResponse]:
        stmt = None
        if folder_uid is None:
            stmt = select(Folder).where(
                (Folder.deleted_at.is_(None))
            )
        else:
            stmt = select(Folder).where(
                (Folder.deleted_at.is_(None))
                & (Folder.uuid == folder_uid)
            )
        result = await session.execute(stmt)
        folders = result.scalars().all()

        return [
            FolderResponse(uuid=f.uuid, folder_name=f.name)
            for f in folders
        ]

    async def make_folder(
        session: AsyncSession, name: str
    ) -> list[FolderResponse]:
        folder = Folder(name=name)
        session.add(folder)
        await session.commit()
        return FolderResponse(
            uuid=folder.uuid, folder_name=folder.name
        )

    async def update_folder(
        session: AsyncSession, folder_uid: str, name: str
    ) -> Optional[FolderResponse]:
        folder = await session.get(Folder, folder_uid)
        if folder:
            folder.name = name
            await session.commit()
        return FolderResponse(
            uuid=folder.uuid, folder_name=folder.name
        )

    async def delete_folder(
        session: AsyncSession, folder_uid: str
    ) -> None:
        stmt = (
            update(Folder)
            .where(Folder.uuid == folder_uid)
            .values(deleted_at=datetime.now())
        )
        await session.execute(stmt)
        await session.commit()
