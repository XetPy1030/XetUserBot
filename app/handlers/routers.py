import asyncio
from datetime import datetime

import arrow
from loguru import logger
from telethon import events

from app.database.models import GoalTimeMessageChat, RepeatMessage
from app.settings import DEFAULT_LOCALE
from app.utils.goal import format_goal_message
from app.utils.time import parse_timedelta


async def ping_handler(event: events.NewMessage.Event):
    respond = await event.respond("Pong")
    await asyncio.sleep(5)
    await event.delete()
    await respond.delete()


async def id_handler(event: events.NewMessage.Event):
    await event.respond(f"Chat id: {event.chat_id}")

    reply = await event.get_reply_message()
    if reply:
        await event.respond(f"Reply message id: {reply.id}")
    else:
        await event.respond("No reply message")


async def delete_all_goal_handler(event: events.NewMessage.Event):
    await GoalTimeMessageChat.all().delete()
    logger.info("All goals deleted")
    await event.respond("All goals deleted")


async def new_goal_handler(event: events.NewMessage.Event):
    cmd, goal_time_text, goal_name = event.text.split(" ", 2)
    goal_time = datetime.fromisoformat(goal_time_text)

    last_text = arrow.get(goal_time).humanize(locale=DEFAULT_LOCALE)
    goal = await GoalTimeMessageChat.create(
        name=goal_name,
        chat_id=event.chat_id,
        message_id=event.id,
        goal_time=goal_time,
        last_text=last_text,
    )
    logger.info(f"Goal created: {goal}")

    await event.edit(format_goal_message(last_text))


async def goals_handler(event: events.NewMessage.Event):
    goals = await GoalTimeMessageChat.filter(is_active=True).all()
    goals_text = "\n".join([f"{goal.name}({goal.id}): {goal.last_text}" for goal in goals])
    await event.respond(goals_text or "No goals")


async def force_new_goal_handler(event: events.NewMessage.Event):
    cmd, name, chat_id, message_id, goal_time_text = event.text.split(" ", 4)
    chat_id = int(chat_id)
    message_id = int(message_id)
    goal_time = datetime.fromisoformat(goal_time_text)

    goal = await GoalTimeMessageChat.create(
        name=name,
        chat_id=chat_id,
        message_id=message_id,
        goal_time=goal_time,
        last_text="",
    )
    logger.info(f"Goal created: {goal}")

    await event.respond("Goal created")


async def repeat_handler(event: events.NewMessage.Event):
    cmd, time_text, text = event.text.split(" ", 2)
    time = parse_timedelta(time_text)

    repeat = await RepeatMessage.create(
        text=text,
        chat_id=event.chat_id,
        time=time,
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
