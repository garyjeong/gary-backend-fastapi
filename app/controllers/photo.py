import os
import uuid
from datetime import datetime
from typing import List

from fastapi import Request
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.config import get_image_host_url
from app.models.folder import Folder
from app.models.photo import Photo
from app.schemas.photo import PhotoResponse


class PhotoController:
    async def get_photo(
        session: AsyncSession,
        folder_uid: str,
        photo_uid: str,
    ) -> list[PhotoResponse]:
        stmt = None
        if folder_uid is None and photo_uid is None:
            # 폴더와 상관없이 전체 사진 가져오기
            stmt = select(Photo).where(
                Photo.deleted_at.is_(None)
            )
        elif folder_uid is not None and photo_uid is None:
            # 지정 폴더에 대한 사진 가져오기
            stmt = select(Photo).where(
                Photo.deleted_at.is_(None)
                & (Photo.folder_uuid == folder_uid)
            )
        else:
            # 지정 폴더에 대한 지정 사진 가져오기
            stmt = select(Photo).where(
                (Photo.deleted_at.is_(None))
                & (Photo.uuid == photo_uid)
                & (Photo.folder_uuid == folder_uid)
            )
        result = await session.execute(stmt)
        photos = result.scalars().all()

        return [
            PhotoResponse(
                uuid=p.uuid, memo=p.memo, url=p.url
            )
            for p in photos
        ]

    async def make_photos(
        session: AsyncSession,
        folder_uid: str = None,
        files: any = None,
    ) -> list[PhotoResponse]:
        folder = None
        if folder_uid:
            stmt = select(Folder).where(
                (Folder.deleted_at.is_(None))
                & (Folder.uuid == folder_uid)
            )
            result = await session.execute(stmt)
            folder = result.scalars().all()[0]
        else:
            stmt = select(Folder).where(
                (Folder.deleted_at.is_(None))
                & (Folder.name == "default")
            )
            result = await session.execute(stmt)
            folder = result.scalars().all()[0]

        save_dir = "photos"

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        photos = []
        image_host = get_image_host_url()
        for file in files:
            u = uuid.uuid4()
            filename = str(u).replace("-", "")

            local_path = os.path.join(
                save_dir, f"{filename}.png"
            )

            with open(local_path, "wb") as buffer:
                buffer.write(await file.read())

            photo = Photo(
                url=f"{image_host}/{local_path}",
                folder_uuid=folder.uuid,
            )
            session.add(photo)
            photos.append(photo)

        await session.commit()
        return [
            PhotoResponse(
                uuid=p.uuid, memo=p.memo, url=p.url
            )
            for p in photos
        ]

    async def update_photo(
        session: AsyncSession, photo_uid: str, memo: str
    ) -> PhotoResponse:
        if photo_uid is None:
            raise "사진을 찾을 수 없습니다."

        stmt = select(Photo).where(
            (Photo.deleted_at.is_(None))
            & (Photo.uuid == photo_uid)
        )
        result = await session.execute(stmt)
        photo = result.scalar_one()
        photo.memo = memo

        await session.commit()
        return PhotoResponse(
            uuid=photo.uuid,
            memo=photo.memo,
        )

    async def move_photo(
        session: AsyncSession,
        folder_id: str,
        photos: List[str],
    ) -> list[PhotoResponse]:
        results = []
        for photo_uid in photos:
            if photo_uid is None:
                raise "사진을 찾을 수 없습니다."

            stmt = select(Photo).where(
                (Photo.deleted_at.is_(None))
                & (Photo.uuid == photo_uid)
            )
            result = await session.execute(stmt)
            photo = result.scalar_one()
            photo.folder_uuid = folder_id
            results.append(photo[0])

        await session.commit()
        return [
            PhotoResponse(
                uuid=p.uuid,
                memo=p.memo,
                folder_uid=p.folder_uid,
            )
            for p in result
        ]

    async def delete_photo(
        session: AsyncSession, photo_uid: str
    ) -> None:
        stmt = (
            update(Photo)
            .where(Photo.uuid == photo_uid)
            .values(delete_at=datetime.now())
        )
        await session.execute(stmt)
        await session.commit()
