from typing import List, Optional
from uuid import UUID

from fastapi import (
    APIRouter,
    Body,
    Depends,
    File,
    Query,
    Request,
    UploadFile,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.photo import PhotoController
from app.database.deps import get_async_session
from app.schemas.photo import PhotoResponse


photo_router = APIRouter(prefix="/photo", tags=["Photos"])


@photo_router.get(
    path="",
    summary="모든 사진 또는 폴더의 사진 가져오기",
    response_model=list[PhotoResponse],
)
async def get_photos(
    f: Optional[UUID] = Query(
        None, description="사진 고유 아이디"
    ),
    p: Optional[UUID] = Query(
        None, description="사진 고유 아이디"
    ),
    session: AsyncSession = Depends(get_async_session),
) -> list[PhotoResponse]:
    return await PhotoController.get_photo(
        session=session,
        folder_uid=str(f) if f is not None else None,
        photo_uid=str(p) if p is not None else None,
    )


@photo_router.post(
    path="",
    summary="사진 업로드",
    response_model=list[PhotoResponse],
)
async def make_photo(
    f: Optional[UUID] = Query(
        None, description="폴더 고유 아이디"
    ),
    files: List[UploadFile] = File(...),
    session: AsyncSession = Depends(get_async_session),
) -> list[PhotoResponse]:
    return await PhotoController.make_photos(
        session=session,
        folder_uid=str(f) if f is not None else None,
        files=files,
    )


@photo_router.patch(
    path="",
    summary="사진 메모 수정",
    response_model=list[PhotoResponse],
)
async def update_photo(
    p: UUID = Query(None, description="사진 고유 아이디"),
    body: dict = Body("memo", description="변경할 메모"),
    session: AsyncSession = Depends(get_async_session),
) -> list[PhotoResponse]:
    return await PhotoController.update_photo(
        session=session,
        photo_uid=str(p) if p is not None else None,
        memo=body["memo"],
    )


@photo_router.patch(
    path="/move",
    summary="다중으로 사진의 폴더를 이동",
    response_model=list[PhotoResponse],
)
async def move_photo(
    f: UUID = Query(None, description="이동할 폴더의 고유 아이디"),
    body=Body("photos", description="이동할 파일들의 고유 아이디"),
    session: AsyncSession = Depends(get_async_session),
) -> list[PhotoResponse]:
    return await PhotoController.move_photo(
        session=session,
        folder_id=str(f) if f is not None else None,
        photos=body["photos"],
    )


@photo_router.delete(
    path="", summary="사진 삭제", response_model=None
)
async def delete_photo(
    p: UUID = Query(None, description="사진의 고유 아이디"),
    session: AsyncSession = Depends(get_async_session),
) -> None:
    return await PhotoController.delete_photo(
        session=session,
        photo_uid=str(p) if p is not None else None,
    )
