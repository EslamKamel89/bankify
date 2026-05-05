from fastapi import APIRouter, Request
from backend.app.core.logging import logger
from backend.app.tasks.example import add

router = APIRouter(prefix="/test", tags=["test"])


@router.get("/logging")
async def test_logging(request: Request):
    logger.info("This is info message")
    logger.debug("This is debug message")
    logger.warning("This is warning message")
    logger.critical("This is critical message")
    logger.error("This is error message")
    return {"message": "logging completed successfully"}


@router.get("/celery_worker")
async def test_celery_worker(request: Request):
    add.delay(2, 4)  # type: ignore
    return {"message": "celery task is triggered"}
