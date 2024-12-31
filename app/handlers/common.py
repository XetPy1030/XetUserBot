import asyncio

from telethon import events


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
