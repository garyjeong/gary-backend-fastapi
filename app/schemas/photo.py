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
