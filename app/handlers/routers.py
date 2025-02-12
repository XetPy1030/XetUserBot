from dataclasses import dataclass

from app import handlers


@dataclass
class Router:
    command: str
    handler: callable
    description: str | None = None
    example_args: str | None = None


routers = [
    Router('ping', handlers.common.ping_handler, 'Ping command'),
    Router('id', handlers.common.id_handler, 'Get chat id'),
    Router('delete_all_goals', handlers.goals.delete_all_goal_handler, 'Delete all goals'),
    Router('new_goal', handlers.goals.new_goal_handler, 'Create new goal', '2025-02-14T03:00:00+03:00 New Goal!'),
    Router('goals', handlers.goals.goals_handler, 'List all goals'),
    Router('force_new_goal', handlers.goals.force_new_goal_handler, 'Force create new goal', 'Goal 828282 1 2025-02-14T03:00:00+03:00'),
    Router('repeat', handlers.repeats.repeat_handler, 'Create repeat message', '1h Repeat'),
    Router('disable_repeat', handlers.repeats.disable_repeat_handler, 'Disable repeat message', '1'),
    Router('repeats', handlers.repeats.repeats_handler, 'List all repeat messages'),
    Router('new_schedule', handlers.schedules.new_schedule_handler, 'Create schedule message', '2025-02-14T03:00:00+03:00 Schedule'),
    Router('disable_schedule', handlers.schedules.disable_schedule_handler, 'Disable schedule message', '1'),
    Router('schedules', handlers.schedules.schedules_handler, 'List all schedule messages'),
]
