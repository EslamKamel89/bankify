from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.api.main import api_router
from backend.app.core.config import settings
from backend.app.core.db import dispose_db, init_db
from backend.app.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("performing initialization procedure")
    await init_db()
    yield
    logger.info("Shutting down, performing essential cleanup")
    await dispose_db()


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
