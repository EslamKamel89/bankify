from celery import Celery
from backend.app.core.config import settings

celery_app = Celery(
    "bankify",
    broker=settings.REDIS_BROKER_URL,
    backend=settings.REDIS_BACKEND_URL,
)
celery_app.set_default()

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    beat_schedule_filename="/tmp/celerybeat-schedule",
)
# if i didn't add the import manually the task is not auto discovered.
import backend.app.tasks.example

celery_app.autodiscover_tasks(["backend.app.tasks"])
celery_app.conf.beat_schedule = {
    "run-every-30-seconds": {
        "task": "backend.app.tasks.example.add",
        "task": "tasks.add",
        "schedule": 10.0,
        "args": (2, 3),
    },
}
