from datetime import datetime

from loguru import logger
from telethon import events

from app.database.models import ScheduleMessage
from app.telegram_client import client
from app.utils.chat import get_chat_id


async def new_schedule_handler(event: events.NewMessage.Event):
    cmd, time_text, text = event.text.split(" ", 2)
    schedule_time = datetime.fromisoformat(time_text)

    chat_id, username = await get_chat_id(event)

    schedule = await ScheduleMessage.create(
        text=text,
        chat_id=chat_id,
        username=username,
        send_time=schedule_time,
    )
    logger.info(f"Schedule created: {schedule}")

    await event.delete()
    await client.send_message("me", f"Schedule created {schedule.id}")


async def disable_schedule_handler(event: events.NewMessage.Event):
    cmd, schedule_id = event.text.split(" ", 1)
    schedule_id = int(schedule_id)

    schedule = await ScheduleMessage.get_or_none(id=schedule_id)
    if schedule:
        schedule.is_active = False
        await schedule.save()
        logger.info(f"Schedule disabled: {schedule}")

        await event.respond("Schedule disabled")
    else:
        await event.respond("Schedule not found")


async def schedules_handler(event: events.NewMessage.Event):
    schedules = await ScheduleMessage.filter(is_active=True).all()
    schedules_text = "\n".join([f"{schedule.id}: {schedule.text}({schedule.send_time})" for schedule in schedules])
    await event.respond(schedules_text or "No active schedules")
