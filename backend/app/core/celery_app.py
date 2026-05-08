from celery import Celery
from backend.app.core.celery_settings import celery_settings
from backend.app.core.config import settings
from kombu import Exchange, Queue

celery_app = Celery(
    "bankify",
    broker=settings.RABBITMQ_BROKER_URL,
    backend=settings.REDIS_BACKEND_URL,
)
celery_app.set_default()

celery_app.conf.update(**celery_settings.to_celery_dict())


# if i didn't add the import manually the task is not auto discovered.
import backend.app.tasks.example

celery_app.autodiscover_tasks(
    [
        "backend.app.tasks",
        # "backend.app.core.emails" ,
    ],
    related_name="tasks",
    force=True,
)
celery_app.conf.task_queues = (
    Queue(
        "bankify_tasks",
        Exchange("bankify_tasks"),
        routing_key="bankify_tasks",
        durable=True,
    ),
)

# celery_app.conf.beat_schedule = {
#     "run-every-30-seconds": {
#         # "task": "backend.app.tasks.example.add",
#         "task": "tasks.add",
#         "schedule": 10.0,
#         "args": (2, 3),
#     },
# }
