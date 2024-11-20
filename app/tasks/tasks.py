from asgiref.sync import async_to_sync

from . import celery_app
from .. import database
from ..utils.goal import check_update_goal


@celery_app.task
def check_update_goal_task():
    async_to_sync(async_check_update_goal)()


async def async_check_update_goal():
    await database.init()
    try:
        await check_update_goal()
    finally:
        await database.close()
