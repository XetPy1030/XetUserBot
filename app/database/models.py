from tortoise import models, fields


class GoalTimeMessageChat(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    chat_id = fields.IntField()
    message_id = fields.IntField()
    goal_time = fields.DatetimeField()

    last_text = fields.TextField()
    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "goal_time_message_chat"
