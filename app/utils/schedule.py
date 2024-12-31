from loguru import logger
from tortoise.timezone import now

from app.database.models import ScheduleMessage
from app.utils.tg import send_message


async def check_schedule():
    schedules = await ScheduleMessage.filter(is_active=True)
    for schedule in schedules:
        schedule: ScheduleMessage

        if schedule.send_time < now():
            logger.info(f"Отправляем сообщение для {schedule.chat}({schedule.id})")

            try:
                await send_message(schedule.chat, schedule.text)
            except Exception as e:
                logger.error(f"Ошибка при отправке сообщения для {schedule.chat}({schedule.id}): {e}")
                continue

            schedule.is_active = False
            await schedule.save()
        else:
            logger.debug(f"Пропускаем сообщение для {schedule.chat}({schedule.id})")
