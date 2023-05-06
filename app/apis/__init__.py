from fastapi import APIRouter

from app.apis.folder import folder_router
from app.apis.photo import photo_router

router = APIRouter()
router.include_router(folder_router)
router.include_router(photo_router)
