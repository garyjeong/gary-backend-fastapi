from uuid import UUID
from pydantic import BaseModel


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
