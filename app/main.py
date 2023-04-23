from fastapi import FastAPI

from app.apis import router


def register_router(application: FastAPI):
    application.include_router(router=router)


def create_application() -> FastAPI:
    application = FastAPI(
        title="Gary API",
        version="1.0.0",
        openapi_url="/openapi.json",
        redoc_url="/redoc",
        docs_url="/docs",
    )
    register_router(application)
    return application


app = create_application()
