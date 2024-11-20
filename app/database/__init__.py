from tortoise import Tortoise


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.database.models']}
    )
    # Генерируем схемы
    await Tortoise.generate_schemas()
