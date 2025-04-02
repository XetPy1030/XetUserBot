from loguru import logger
from telethon import events

from app.database.models import ReactionForUser


async def new_reaction_for_user_handler(event: events.NewMessage.Event):
    if not isinstance(event.text, str):
        await event.respond("Invalid input")
        return

    reply = await event.get_reply_message()
    if not reply:
        await event.respond("Please reply to a message from the user you want to add reaction for")
        return

    try:
        cmd, reaction = event.text.split(" ", 1)
    except ValueError:
        await event.respond("Please provide the command, reaction in the format: /cmd reaction")
        return

    if not reaction:
        await event.respond("Reaction for user cannot be empty")
        return

    reaction_for_user = await ReactionForUser.create(user_id=reply.sender_id, reaction=reaction)
    logger.info(f"New reaction for user: {reaction_for_user}")
    await event.respond("Reaction for user created")


async def disable_reaction_for_user_handler(event: events.NewMessage.Event):
    if not isinstance(event.text, str):
        await event.respond("Invalid input")
        return

    cmd, reaction_id = event.text.split(" ", 1)
    reaction_id = int(reaction_id)

    reaction_for_user = await ReactionForUser.get_or_none(id=reaction_id)
    if reaction_for_user:
        reaction_for_user.is_active = False
        await reaction_for_user.save()
        logger.info(f"Reaction for user disabled: {reaction_for_user}")
        await event.respond("Reaction for user disabled")
    else:
        await event.respond("Reaction for user not found")


async def reactions_for_user_handler(event: events.NewMessage.Event):
    reaction_for_users = await ReactionForUser.filter(is_active=True)
    if reaction_for_users:
        reactions_text = "\n".join([
            f"ID: {reaction_for_user.id}\n"
            f"User ID: {reaction_for_user.user_id}\n"
            f"Reaction: {reaction_for_user.reaction}\n"
            for reaction_for_user in reaction_for_users
        ])
        await event.respond(f"Active reactions for user:\n\n{reactions_text}")
    else:
        await event.respond("No active reactions for user")
