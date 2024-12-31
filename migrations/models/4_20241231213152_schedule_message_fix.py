from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "schedule_message" ALTER COLUMN "username" DROP NOT NULL;
        ALTER TABLE "schedule_message" ALTER COLUMN "chat_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "schedule_message" ALTER COLUMN "username" SET NOT NULL;
        ALTER TABLE "schedule_message" ALTER COLUMN "chat_id" SET NOT NULL;"""
