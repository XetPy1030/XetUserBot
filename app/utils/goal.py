import arrow
from loguru import logger
from tortoise.timezone import now

from app.database.models import GoalTimeMessageChat
from app.settings import DEFAULT_LOCALE
from app.utils.tg import edit_message

GOAL_MESSAGE_FORMAT = "{time}."


async def check_update_goal():
    chats = await GoalTimeMessageChat.filter(is_active=True)
    for chat in chats:
        chat: GoalTimeMessageChat

        if chat.goal_time < now():
            logger.info(f"Время вышло для {chat.chat_id} {chat.message_id}")

            chat.is_active = False
            await chat.save()

            await edit_message(chat.chat_id, chat.message_id, "Время вышло.")

            continue

        text = arrow.get(chat.goal_time).humanize(locale=DEFAULT_LOCALE)
        if text != chat.last_text:
            logger.info(f"Обновляем сообщение для {chat.chat_id} {chat.message_id}")

            chat.last_text = text
            await chat.save()

            await edit_message(chat.chat_id, chat.message_id, format_goal_message(text))


def format_goal_message(goal_text: str):
    return GOAL_MESSAGE_FORMAT.format(time=goal_text).capitalize()
