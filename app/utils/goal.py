from contextlib import asynccontextmanager

import arrow
from loguru import logger
from tortoise.timezone import now

from app.database import GoalTimeMessageChat
from app.settings import DEFAULT_LOCALE
from app.telegram_client import generate_client, start_telegram_client

GOAL_MESSAGE_FORMAT = "{time}."


async def check_update_goal():
    chats = await GoalTimeMessageChat.filter(is_active=True)
    for chat in chats:
        chat: GoalTimeMessageChat

        if chat.goal_time < now():
            logger.info(f"Время вышло для {chat.chat_id} {chat.message_id}")

            chat.is_active = False
            await chat.save()

            await edit_message(chat, "Время вышло.")

            continue

        text = arrow.get(chat.goal_time).humanize(locale=DEFAULT_LOCALE)
        if text != chat.last_text:
            logger.info(f"Обновляем сообщение для {chat.chat_id} {chat.message_id}")

            chat.last_text = text
            await chat.save()

            await edit_message(chat, format_goal_message(text))


def format_goal_message(goal_text: str):
    return GOAL_MESSAGE_FORMAT.format(time=goal_text).capitalize()


async def edit_message(chat: GoalTimeMessageChat, message: str):
    async with celery_tg_client() as tg_client:
        tg_chat = await tg_client.get_entity(chat.chat_id)
        tg_message = await tg_client.get_messages(tg_chat, ids=chat.message_id)
        await tg_message.edit(message)


@asynccontextmanager
async def celery_tg_client():
    tg_client = generate_client('session_celery')
    await start_telegram_client(tg_client)
    try:
        yield tg_client
    finally:
        await tg_client.disconnect()
