from celery import Celery

from app.core.settings import settings

app = Celery(
    "tasks", broker=settings.database.REDIS_URL, backend=settings.database.REDIS_URL
)

from app.services.resume import resume_tasks  # noqa
# from app.services.chatbot import chatbot_tasks  # noqa


app.autodiscover_tasks()