from fastapi import APIRouter

from backend.app.core.logging import logger

router = APIRouter(prefix="/home", tags=["home"])


@router.get("/")
def home():
    logger.info("This is info message")
    logger.debug("This is debug message")
    logger.warning("This is warning message")
    logger.critical("This is critical message")
    logger.error("This is error message")
    return {"message": "Welcome to Bankify, YOUR all in one ERP system"}
