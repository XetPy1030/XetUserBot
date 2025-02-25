from loguru import logger
from telethon import events

from app.database.models import ReactionText


async def new_reaction_handler(event: events.NewMessage.Event):
    if not isinstance(event.text, str):
        await event.respond("Invalid input")
        return

    try:
        cmd, reaction, text = event.text.split(" ", 2)
    except ValueError:
        await event.respond("Please provide the command, reaction, and text in the format: /cmd reaction text")
        return

    if not text or not reaction:
        await event.respond("Reaction and text cannot be empty")
        return

    reaction_text = await ReactionText.create(text=text, reaction=reaction)
    logger.info(f"New reaction: {reaction_text}")
    await event.respond("Reaction created")


async def disable_reaction_handler(event: events.NewMessage.Event):
    if not isinstance(event.text, str):
        await event.respond("Invalid input")
        return

    cmd, reaction_id = event.text.split(" ", 1)
    reaction_id = int(reaction_id)

    reaction_text = await ReactionText.get_or_none(id=reaction_id)
    if reaction_text:
        reaction_text.is_active = False
        await reaction_text.save()
        logger.info(f"Reaction disabled: {reaction_text}")
        await event.respond("Reaction disabled")
    else:
        await event.respond("Reaction not found")


async def reactions_handler(event: events.NewMessage.Event):
    reaction_texts = await ReactionText.filter(is_active=True)
    if reaction_texts:
        reactions_text = "\n".join(
            [f"ID: {reaction_text.id}\nText: {reaction_text.text}\nReaction: {reaction_text.reaction}\n" for
             reaction_text in reaction_texts])
        await event.respond(f"Active Reactions:\n\n{reactions_text}")
    else:
        await event.respond("No active reactions")
