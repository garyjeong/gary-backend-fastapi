from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.folder import FolderController
from app.database.deps import get_async_session
from app.schemas.folder import CreateFolder, UpdateFolder

folder_router = APIRouter(prefix="/folder", tags=["Folders"])


@folder_router.get(path="", summary="모든 폴더 가져오기")
async def get_folder(
    f: Optional[UUID] = Query(None, description="폴더 고유 아이디"),
    session: AsyncSession = Depends(get_async_session),
):
    return await FolderController.get_folder(session, uuid=f)


@folder_router.post(path="", summary="폴더 생성")
async def make_folder(
    data: CreateFolder, session: AsyncSession = Depends(get_async_session)
):
    return await FolderController.make_folder(session=session, name=data.name)


@folder_router.patch(path="")
async def update_folder(
    data: UpdateFolder,
    f: UUID = Query(..., description="폴더 고유 아이디"),
    session: AsyncSession = Depends(get_async_session),
):
    return await FolderController.update_folder(session=session, uuid=f, name=data.name)


@folder_router.delete(path="")
async def delete_folder(
    f: UUID = Query(..., description="폴더 고유 아이디"),
    session: AsyncSession = Depends(get_async_session),
):
    return await FolderController.delete_folder(session=session, uuid=f)
