from fastapi import APIRouter

from app.apis.photo import photo_router

router = APIRouter(
    prefix="/api",
    tags=["Api"],
    # include_in_schema=True,
)
router.include_router(photo_router)
