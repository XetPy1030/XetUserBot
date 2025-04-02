from dataclasses import dataclass

from app.handlers import common, goals, repeats, schedules, reaction, reaction_for_user


@dataclass
class Router:
    command: str
    handler: callable
    description: str | None = None
    example_args: str | None = None


routers = [
    Router('ping', common.ping_handler, 'Ping command'),
    Router('id', common.id_handler, 'Get chat id'),
    Router('delete_all_goals', goals.delete_all_goal_handler, 'Delete all goals'),
    Router('new_goal', goals.new_goal_handler, 'Create new goal', '2025-02-14T03:00:00+03:00 New Goal!'),
    Router('goals', goals.goals_handler, 'List all goals'),
    Router('force_new_goal', goals.force_new_goal_handler, 'Force create new goal', 'Goal 828282 1 2025-02-14T03:00:00+03:00'),
    Router('repeat', repeats.repeat_handler, 'Create repeat message', '1h Repeat'),
    Router('disable_repeat', repeats.disable_repeat_handler, 'Disable repeat message', '1'),
    Router('repeats', repeats.repeats_handler, 'List all repeat messages'),
    Router('new_schedule', schedules.new_schedule_handler, 'Create schedule message', '2025-02-14T03:00:00+03:00 Schedule'),
    Router('disable_schedule', schedules.disable_schedule_handler, 'Disable schedule message', '1'),
    Router('schedules', schedules.schedules_handler, 'List all schedule messages'),
    Router('new_reaction', reaction.new_reaction_handler, 'Create reaction', 'reaction trigger_text'),
    Router('disable_reaction', reaction.disable_reaction_handler, 'Disable reaction', '1'),
    Router('reactions', reaction.reactions_handler, 'List all reactions'),
    Router('new_reaction_for_user', reaction_for_user.new_reaction_for_user_handler, 'Create reaction for user', 'reaction'),
    Router('disable_reaction_for_user', reaction_for_user.disable_reaction_for_user_handler, 'Disable reaction for user', '1'),
    Router('reactions_for_user', reaction_for_user.reactions_for_user_handler, 'List all reactions for user'),
]
