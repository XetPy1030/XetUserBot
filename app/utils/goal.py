import arrow
from loguru import logger
from telethon import TelegramClient
from tortoise.timezone import now

from app.database import GoalTimeMessageChat
from app.settings import DEFAULT_LOCALE

GOAL_MESSAGE_FORMAT = "{time}."


async def check_update_goal(tg_client: TelegramClient):
    chats = await GoalTimeMessageChat.filter(is_active=True)
    for chat in chats:
        chat: GoalTimeMessageChat

        if chat.goal_time < now():
            logger.info(f"Время вышло для {chat.chat_id} {chat.message_id}")

            chat.is_active = False
            await chat.save()

            await edit_message(tg_client, chat, "Время вышло.")

            continue

        text = arrow.get(chat.goal_time).humanize(locale=DEFAULT_LOCALE)
        if text != chat.last_text:
            logger.info(f"Обновляем сообщение для {chat.chat_id} {chat.message_id}")

            chat.last_text = text
            await chat.save()

            await edit_message(tg_client, chat, format_goal_message(text))


def format_goal_message(goal_text: str):
    return GOAL_MESSAGE_FORMAT.format(time=goal_text).capitalize()


async def edit_message(tg_client: TelegramClient, chat: GoalTimeMessageChat, message: str):
    tg_chat = await tg_client.get_entity(chat.chat_id)
    tg_message = await tg_client.get_messages(tg_chat, ids=chat.message_id)
    await tg_message.edit(message)
