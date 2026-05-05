from celery import shared_task
from backend.app.core.celery_app import celery_app
from backend.app.core.logging import logger


# @celery_app.task(name="tasks.add")
@shared_task(name="tasks.add")
def add(x: int, y: int) -> int:
    result = x + y
    # print(result)
    logger.info(f"Example task result is {result}")
    return result
