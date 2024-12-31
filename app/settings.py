import os

from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
TELEGRAM_PASSWORD = os.getenv("TELEGRAM_PASSWORD")

os.environ.setdefault("USE_TZ", "True")

DB_URL = os.getenv("DB_URL") or "postgres://postgres:postgres@localhost:5432/postgres"

DEFAULT_LOCALE = "ru"

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL") or "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND") or "redis://localhost:6379/0"

CELERY_BEAT_SCHEDULE = {
    "check_update_goal": {
        "task": "app.tasks.tasks.check_update_goal_task",
        "schedule": crontab(minute="*"),
    },
    "check_update_repeat": {
        "task": "app.tasks.tasks.check_update_repeat_task",
        "schedule": crontab(minute="*"),
    },
    "check_schedule": {
        "task": "app.tasks.tasks.check_schedule_task",
        "schedule": crontab(minute="*"),
    },
}
