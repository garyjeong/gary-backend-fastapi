from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.folder import FolderController
from app.database.deps import get_async_session
from app.schemas.folder import CreateFolder, UpdateFolder
from app.schemas.folder import FolderResponse

folder_router = APIRouter(
    prefix="/folder", tags=["Folders"]
)


@folder_router.get(
    path="",
    summary="모든 폴더 가져오기",
    response_model=list[FolderResponse],
)
async def get_folder(
    f: Optional[UUID] = Query(
        None, description="폴더 고유 아이디"
    ),
    session: AsyncSession = Depends(get_async_session),
) -> list[FolderResponse]:
    return await FolderController.get_folder(
        session,
        folder_uid=str(f) if f is not None else None,
    )


@folder_router.post(
    path="", summary="폴더 생성", response_model=FolderResponse
)
async def make_folder(
    data: CreateFolder,
    session: AsyncSession = Depends(get_async_session),
) -> FolderResponse:
    return await FolderController.make_folder(
        session=session, name=data.name
    )


@folder_router.patch(
    path="",
    summary="폴더 이름 수정",
    response_model=FolderResponse,
)
async def update_folder(
    data: UpdateFolder,
    f: UUID = Query(..., description="폴더 고유 아이디"),
    session: AsyncSession = Depends(get_async_session),
) -> FolderResponse:
    return await FolderController.update_folder(
        session=session,
        folder_uid=str(f) if f is not None else None,
        name=data.name,
    )


@folder_router.delete(
    path="", summary="폴더 삭제", response_model=None
)
async def delete_folder(
    f: UUID = Query(..., description="폴더 고유 아이디"),
    session: AsyncSession = Depends(get_async_session),
) -> None:
    return await FolderController.delete_folder(
        session=session,
        folder_uid=str(f) if f is not None else None,
    )
