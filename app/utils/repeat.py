from asyncpg.pgproto.pgproto import timedelta
from loguru import logger
from tortoise.timezone import now

from app.database.models import RepeatMessage
from app.utils.tg import send_message


async def check_update_repeat():
    repeat_messages = await RepeatMessage.filter(is_active=True)
    for repeat_message in repeat_messages:
        repeat_message: RepeatMessage

        if (
            repeat_message.last_send is None or
            # - 10 секунд, чтобы не пропустить сообщение
            (repeat_message.last_send + repeat_message.repeat_time - timedelta(seconds=10)) < now()
        ):
            logger.info(f"Отправляем сообщение для {repeat_message.chat}({repeat_message.id})")

            try:
                await send_message(repeat_message.chat, repeat_message.text)
            except Exception as e:
                logger.error(f"Ошибка при отправке сообщения для {repeat_message.chat}({repeat_message.id}): {e}")
                continue

            repeat_message.last_send = now()
            await repeat_message.save()
        else:
            logger.debug(f"Пропускаем сообщение для {repeat_message.chat}({repeat_message.id})")
