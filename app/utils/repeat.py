from loguru import logger
from tortoise.timezone import now

from app.database.models import RepeatMessage
from app.utils.tg import send_message


async def check_update_repeat():
    repeat_messages = await RepeatMessage.filter(is_active=True)
    for repeat_message in repeat_messages:
        repeat_message: RepeatMessage

        if repeat_message.last_send is None or repeat_message.last_send + repeat_message.repeat_time < now():
            logger.info(f"Отправляем сообщение для {repeat_message.chat_id}({repeat_message.id})")

            await send_message(repeat_message.chat_id, repeat_message.text)

            repeat_message.last_send = now()
            await repeat_message.save()
        else:
            logger.debug(f"Пропускаем сообщение для {repeat_message.chat_id}({repeat_message.id})")
