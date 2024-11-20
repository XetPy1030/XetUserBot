import asyncio

from loguru import logger

from app import database


def configure_logging():
    pass


async def main():
    configure_logging()

    await database.init()

    logger.info('Starting bot...')


if __name__ == '__main__':
    asyncio.run(main())
