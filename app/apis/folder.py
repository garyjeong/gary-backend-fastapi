from uuid import UUID

from fastapi import APIRouter, Body, Query

from app.controllers.folder import FolderController

folder_router = APIRouter(prefix="/folder", tags=["Folders"])


@folder_router.get()
async def get_folder(f: UUID = Query(..., description="폴더 고유 아이디")):
    return await FolderController.get_folder(uuid=f)


@folder_router.post()
async def make_folder(name: str = Body(..., description="폴더 이름")):
    return await FolderController.make_folder(name=name)


@folder_router.patch()
async def update_folder(
    f: UUID = Query(..., description="폴더 고유 아이디"),
    name: str = Body(..., description="폴더 이름"),
):
    return await FolderController.update_folder(uuid=f, name=name)


@folder_router.delete()
async def delete_folder(f: UUID = Query(..., description="폴더 고유 아이디")):
    return await FolderController.delete_folder(uuid=f)
