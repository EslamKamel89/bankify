import os
import sys

from loguru import logger

from backend.app.core.config import settings

logger.remove()
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
logger.add(
    sys.stdout,
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
)

logger.add(
    os.path.join(LOG_DIR, "debug.log"),
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="DEBUG" if settings.ENVIRONMENT == "local" else "INFO",
)
logger.add(
    os.path.join(LOG_DIR, "error.log"),
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="ERROR",
    backtrace=True,
    diagnose=True,
)

__all__ = ["logger"]
