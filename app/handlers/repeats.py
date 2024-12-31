from loguru import logger
from telethon import events

from app.database.models import RepeatMessage
from app.utils.chat import get_chat_id
from app.utils.time import parse_timedelta


async def repeat_handler(event: events.NewMessage.Event):
    cmd, time_text, text = event.text.split(" ", 2)
    repeat_time = parse_timedelta(time_text)

    chat_id, username = await get_chat_id(event)

    repeat = await RepeatMessage.create(
        text=text,
        chat_id=chat_id,
        username=username,
        repeat_time=repeat_time,
    )
    logger.info(f"Repeat created: {repeat}")

    await event.respond("Repeat created")


async def disable_repeat_handler(event: events.NewMessage.Event):
    cmd, repeat_id = event.text.split(" ", 1)
    repeat_id = int(repeat_id)

    repeat = await RepeatMessage.get_or_none(id=repeat_id)
    if repeat:
        repeat.is_active = False
        await repeat.save()
        logger.info(f"Repeat disabled: {repeat}")

        await event.respond("Repeat disabled")
    else:
        await event.respond("Repeat not found")


async def repeats_handler(event: events.NewMessage.Event):
    repeats = await RepeatMessage.filter(is_active=True).all()
    repeats_text = "\n".join([f"{repeat.id}: {repeat.text}({repeat.repeat_time})" for repeat in repeats])
    await event.respond(repeats_text or "No active repeats")
