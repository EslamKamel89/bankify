from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

# the NAMESPACES is where the acceptable config options exist and the CelerySettings below is a typed version of the important option that exist
# from celery.app.defaults import NAMESPACES


class CelerySettings(BaseModel):
    """
    Production-oriented reusable Celery configuration.
    """

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

    task_serializer: Literal["json"] = Field(
        default="json",
        description=(
            "Serialization format used when sending task payloads "
            "through the message broker."
        ),
    )

    accept_content: list[str] = Field(
        default=["json"],
        description=(
            "Allowed serialization formats accepted by workers. "
            "Restricting to JSON improves security by preventing "
            "pickle-based remote code execution."
        ),
    )

    result_serializer: Literal["json"] = Field(
        default="json",
        description=(
            "Serialization format used for storing task results "
            "inside the result backend."
        ),
    )

    timezone: str = Field(
        default="UTC",
        description=("Timezone used by Celery Beat and scheduling systems."),
    )

    enable_utc: bool = Field(
        default=True,
        description=("Force Celery internals to normalize timestamps to UTC."),
    )

    beat_schedule_filename: str = Field(
        default="/tmp/celerybeat-schedule",
        description=("Persistent storage file used by Celery Beat scheduler."),
    )

    result_backend_max_retries: int = Field(
        default=10,
        description=(
            "Maximum retry attempts when communicating with " "the result backend."
        ),
    )

    result_backend_always_retry: bool = Field(
        default=True,
        description=("Retry result backend operations instead of failing immediately."),
    )

    result_expires: int = Field(
        default=3600,
        description=(
            "How long task results remain stored before expiration " "(in seconds)."
        ),
    )

    result_extended: bool = Field(
        default=True,
        description=(
            "Store extended task metadata including worker info, "
            "arguments, retries, and execution details."
        ),
    )

    task_track_started: bool = Field(
        default=True,
        description=("Track STARTED state in addition to SUCCESS/FAILURE."),
    )

    task_send_sent_event: bool = Field(
        default=True,
        description=(
            "Emit task-sent monitoring events for observability tools " "like Flower."
        ),
    )

    task_soft_time_limit: int = Field(
        default=300,
        description=(
            "Graceful execution timeout in seconds. "
            "Raises SoftTimeLimitExceeded inside task."
        ),
    )

    task_time_limit: int = Field(
        default=360,
        description=(
            "Hard execution timeout in seconds. "
            "Worker forcibly terminates task after this limit."
        ),
    )

    task_acks_late: bool = Field(
        default=True,
        description=(
            "Acknowledge tasks AFTER execution instead of before. "
            "Improves crash recovery but tasks must be idempotent."
        ),
    )

    task_reject_on_worker_lost: bool = Field(
        default=True,
        description=("Requeue tasks if worker crashes before acknowledging."),
    )

    worker_prefetch_multiplier: int = Field(
        default=1,
        description=(
            "Number of tasks reserved per worker process. "
            "Lower values improve fairness for long-running tasks."
        ),
    )

    task_default_queue: str = Field(
        default="bankify_tasks",
        description=("Default queue used for task routing."),
    )

    task_create_missing_queues: bool = Field(
        default=False,
        description=("Automatically create queues referenced by task routes."),
    )

    worker_max_tasks_per_child: int = Field(
        default=1000,
        description=(
            "Recycle worker process after processing N tasks. "
            "Helps mitigate memory leaks."
        ),
    )

    worker_max_memory_per_child: int = Field(
        default=250000,
        description=("Maximum memory per worker process in KB before recycle."),
    )

    worker_log_format: str = Field(
        default="[%(asctime)s: %(levelname)s/%(processname)s] %(message)s",
        description=("Log format for worker process logs."),
    )

    worker_task_log_format: str = Field(
        default=(
            "[%(asctime)s: %(levelname)s/%(processname)s]"
            "[%(task_name)s(%(task_id)s)] %(message)s"
        ),
        description=("Log format for task execution logs."),
    )

    broker_connection_retry_on_startup: bool = Field(
        default=True,
        description=(
            "Retry broker connection during startup instead of failing immediately."
        ),
    )
    worker_enable_remote_control: bool = Field(
        default=True,
        description=(
            "Disable remote control queues incompatible with "
            "RabbitMQ 4 transient queue restrictions."
        ),
    )

    worker_send_task_events: bool = Field(
        default=True,
        description=("Disable worker event broadcasting queues."),
    )

    task_default_exchange: str = Field(
        default="bankify_tasks",
        description=("Default exchange used for publishing Celery tasks."),
    )

    task_default_exchange_type: Literal["direct", "topic", "fanout", "headers"] = Field(
        default="direct",
        description=("Exchange routing strategy used for task delivery."),
    )

    task_default_routing_key: str = Field(
        default="bankify_tasks",
        description=("Default routing key used when publishing tasks."),
    )

    def to_celery_dict(self) -> dict:
        """
        Convert settings into a Celery-compatible configuration dictionary.
        """
        return self.model_dump()


celery_settings = CelerySettings()
