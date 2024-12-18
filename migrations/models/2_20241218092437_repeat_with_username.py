from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE repeat_message ALTER COLUMN chat_id DROP NOT NULL;
        ALTER TABLE repeat_message ADD COLUMN username VARCHAR(255) NULL;
        """


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE repeat_message ALTER COLUMN chat_id SET NOT NULL;
        ALTER TABLE repeat_message DROP COLUMN username;
        """
