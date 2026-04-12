from contextlib import asynccontextmanager

import fastapi_swagger_dark as fsd
from fastapi import FastAPI

from backend.app.api.main import api_router
from backend.app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("performing initialization procedure")
    yield
    print("Shutting down, performing essential cleanup")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    lifespan=lifespan,
    docs_url=f"/{settings.API_VERSION}/docs",
    redoc_url=f"/{settings.API_VERSION}/redoc",
    openapi_url=f"/{settings.API_VERSION}/openapi.json",
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(api_router, prefix=f"/{settings.API_VERSION}")
