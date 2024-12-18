from contextlib import asynccontextmanager

import telethon.errors
from loguru import logger
from telethon import TelegramClient

from app.telegram_client import generate_client, start_telegram_client


async def edit_message(chat_id, message_id, message_text: str):
    async with celery_tg_client() as tg_client:
        tg_client: TelegramClient
        tg_chat = await tg_client.get_input_entity(chat_id)

        tg_message = await tg_client.get_messages(tg_chat, ids=message_id)

        try:
            await tg_message.edit(message_text)
        except telethon.errors.rpcerrorlist.MessageEditTimeExpiredError:
            logger.error(f"Не удалось отредактировать сообщение {chat_id} {message_id}: время истекло")


async def send_message(chat_id, message_text: str):
    async with celery_tg_client() as tg_client:
        tg_client: TelegramClient
        tg_chat = await tg_client.get_input_entity(chat_id)

        await tg_client.send_message(tg_chat, message_text)


@asynccontextmanager
async def celery_tg_client():
    tg_client = generate_client('session_celery')
    await start_telegram_client(tg_client)
    try:
        yield tg_client
    finally:
        await tg_client.disconnect()
