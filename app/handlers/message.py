from loguru import logger
from telethon import events, functions, types

from app.database.models import ReactionText, ReactionForUser
from app.telegram_client import client


async def reaction_handler(event: events.NewMessage.Event):
    reaction_texts = await ReactionText.filter(is_active=True)
    for reaction_text in reaction_texts:
        if not isinstance(event.text, str):
            continue

        if reaction_text.text.lower() in event.text.lower():
            logger.info(f"Reaction: {reaction_text.reaction}")
            await client(functions.messages.SendReactionRequest(
                peer=event.message.peer_id,
                msg_id=event.message.id,
                reaction=[types.ReactionEmoji(
                    emoticon=reaction_text.reaction
                )]
            ))
            break
    
    reaction_for_user = await ReactionForUser.filter(is_active=True, user_id=event.sender_id)
    for reaction in reaction_for_user:
        logger.info(f"Reaction: {reaction.reaction}")
        await client(functions.messages.SendReactionRequest(
            peer=event.message.peer_id,
            msg_id=event.message.id,
            reaction=[types.ReactionEmoji(emoticon=reaction.reaction)]
        ))
