import contextlib

from app import database


@contextlib.asynccontextmanager
async def database_session():
    await database.init()
    try:
        yield
    finally:
        await database.close()
