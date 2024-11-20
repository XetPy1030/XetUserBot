from loguru import logger
from telethon import TelegramClient

from app.settings import API_ID, API_HASH, PHONE_NUMBER, TELEGRAM_PASSWORD


def generate_client(session_name):
    return TelegramClient(
        session_name,
        API_ID,
        API_HASH,
        system_version='4.16.30-vxCUSTOM',
        device_model='POCO M4 Pro',
        app_version='1.0',
    )


client: TelegramClient = generate_client('session_name')


async def start_telegram_client(tg_client: TelegramClient) -> None:
    await tg_client.start(phone=PHONE_NUMBER, password=TELEGRAM_PASSWORD)  # noqa
    logger.info('Telegram client started')
