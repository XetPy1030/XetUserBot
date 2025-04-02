from tortoise import models, fields


class GoalTimeMessageChat(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    chat_id = fields.BigIntField()
    message_id = fields.BigIntField()
    goal_time = fields.DatetimeField()

    last_text = fields.TextField()
    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "goal_time_message_chat"


class RepeatMessage(models.Model):
    id = fields.IntField(pk=True)
    text = fields.TextField()
    chat_id = fields.BigIntField(null=True)
    username = fields.CharField(max_length=255, null=True)
    repeat_time = fields.TimeDeltaField()

    last_send = fields.DatetimeField(null=True)
    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    @property
    def chat(self):
        return self.chat_id or self.username

    class Meta:
        table = "repeat_message"


class ScheduleMessage(models.Model):
    id = fields.IntField(pk=True)

    text = fields.TextField()
    chat_id = fields.BigIntField(null=True)
    username = fields.CharField(max_length=255, null=True)
    send_time = fields.DatetimeField()

    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    @property
    def chat(self):
        return self.chat_id or self.username

    class Meta:
        table = "schedule_message"


class ReactionText(models.Model):
    id = fields.IntField(pk=True)

    text = fields.TextField()
    reaction = fields.CharField(max_length=255)

    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reaction_text"


class ReactionForUser(models.Model):
    id = fields.IntField(pk=True)

    user_id = fields.BigIntField()
    reaction = fields.CharField(max_length=255)

    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reaction_for_user"
