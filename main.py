import asyncio

from loguru import logger

from app import database
from app.handlers import setup_routers
from app.telegram_client import start_telegram_client, client


def configure_logging():
    pass


async def main():
    configure_logging()

    logger.info('Initializing database...')
    await database.init()

    logger.info('Starting bot...')
    await start_telegram_client(client)
    setup_routers()

    logger.info('Bot started')
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
