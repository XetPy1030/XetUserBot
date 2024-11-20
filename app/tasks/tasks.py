from asgiref.sync import async_to_sync

from . import celery_app
from .. import database
from ..telegram_client import celery_client as tg_client, start_telegram_client
from ..utils.goal import check_update_goal


@celery_app.task
def check_update_goal_task():
    async_to_sync(async_check_update_goal)()


async def async_check_update_goal():
    await database.init()
    try:
        if not tg_client or not tg_client.is_connected():
            await start_telegram_client(tg_client)

        try:
            await check_update_goal(tg_client)
        finally:
            await tg_client.disconnect()
    finally:
        await database.close()
