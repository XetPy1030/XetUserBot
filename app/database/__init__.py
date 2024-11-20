from tortoise import Tortoise

from app.database.models import GoalTimeMessageChat
from app.settings import DB_URL


async def init():
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['app.database.models']}
    )
    # Генерируем схемы
    await Tortoise.generate_schemas()


async def close():
    await Tortoise.close_connections()
