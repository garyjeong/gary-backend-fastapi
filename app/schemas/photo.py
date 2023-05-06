from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.models.photo import Photo


class GetPhoto(BaseModel):
    uuid: UUID

    class Config:
        orm_mode = True


class CreatePhoto(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UpdatePhoto(BaseModel):
    uuid: UUID
    name: str

    class Config:
        orm_mode = True


class DeletePhoto(BaseModel):
    uuid: UUID

    class Config:
        orm_mode = True


class PhotoResponse(BaseModel):
    uuid: UUID
    memo: Optional[str]
    url: str
    created_at: str
    updated_at: str

    @classmethod
    def from_orm(cls, photo):
        return cls(
            uuid=photo.uuid,
            memo=photo.memo,
            url=photo.url,
            created_at=datetime.strftime(
                photo.created_at, "%Y-%m-%d %H:%M:%S"
            ),
            updated_at=datetime.strftime(
                photo.updated_at, "%Y-%m-%d %H:%M:%S"
            ),
        )
