from telethon.tl.types import User


async def get_chat_id(event):
    chat = await event.get_chat()
    username = chat_id = None
    if isinstance(chat, User) and chat.bot:
        username = chat.username
    else:
        chat_id = event.chat_id
    return chat_id, username
