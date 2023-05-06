from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class GetFolder(BaseModel):
    uuid: UUID

    class Config:
        orm_mode = True


class CreateFolder(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UpdateFolder(BaseModel):
    name: str

    class Config:
        orm_mode = True


class DeleteFolder(BaseModel):
    uuid: UUID

    class Config:
        orm_mode = True


class FolderResponse(BaseModel):
    uuid: UUID
    name: str
    created_at: str
    updated_at: str

    @classmethod
    def from_orm(cls, folder):
        return cls(
            uuid=folder.uuid,
            name=folder.name,
            created_at=datetime.strftime(
                folder.created_at, "%Y-%m-%d %H:%M:%S"
            ),
            updated_at=datetime.strftime(
                folder.updated_at, "%Y-%m-%d %H:%M:%S"
            ),
        )
