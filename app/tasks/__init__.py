from celery import Celery

# Создание экземпляра Celery
celery_app = Celery(
    "app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

# Загрузка конфигурации Celery (если есть)
celery_app.config_from_object("app.settings", namespace="CELERY")

# Автоматический поиск задач в модулях
celery_app.autodiscover_tasks(["app.tasks"])

__all__ = ("celery_app",)
