from asgiref.sync import async_to_sync

from . import celery_app
from ..utils.db import database_session
from ..utils.goal import check_update_goal
from ..utils.repeat import check_update_repeat
from ..utils.schedule import check_schedule


@celery_app.task
def check_update_goal_task():
    async def task():
        async with database_session():
            await check_update_goal()

    async_to_sync(task)()


@celery_app.task
def check_update_repeat_task():
    async def task():
        async with database_session():
            await check_update_repeat()

    async_to_sync(task)()


@celery_app.task
def check_schedule_task():
    async def task():
        async with database_session():
            await check_schedule()

    async_to_sync(task)()
