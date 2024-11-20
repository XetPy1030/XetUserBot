import asyncio

from app.telegram_client import start_telegram_client, client, celery_client


async def main():
    await start_telegram_client(client)
    await start_telegram_client(celery_client)

    client_is_auth = await client.is_user_authorized()
    celery_client_is_auth = await celery_client.is_user_authorized()

    print(f'Client is authorized: {client_is_auth}')
    print(f'Celery client is authorized: {celery_client_is_auth}')


if __name__ == '__main__':
    asyncio.run(main())
