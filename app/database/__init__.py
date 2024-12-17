from tortoise import Tortoise

from app.database.settings import TORTOISE_ORM


async def init():
    await Tortoise.init(TORTOISE_ORM)
    # Генерируем схемы
    await Tortoise.generate_schemas()


async def close():
    await Tortoise.close_connections()
