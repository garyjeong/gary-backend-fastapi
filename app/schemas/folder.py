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
