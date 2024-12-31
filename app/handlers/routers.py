from dataclasses import dataclass

from app import handlers


@dataclass
class Router:
    command: str
    handler: callable
    description: str | None = None


routers = [
    Router('ping', handlers.common.ping_handler, 'Ping command'),
    Router('id', handlers.common.id_handler, 'Get chat id'),
    Router('delete_all_goals', handlers.goals.delete_all_goal_handler, 'Delete all goals'),
    Router('new_goal', handlers.goals.new_goal_handler, 'Create new goal'),
    Router('goals', handlers.goals.goals_handler, 'List all goals'),
    Router('force_new_goal', handlers.goals.force_new_goal_handler, 'Force create new goal'),
    Router('repeat', handlers.repeats.repeat_handler, 'Create repeat message'),
    Router('disable_repeat', handlers.repeats.disable_repeat_handler, 'Disable repeat message'),
    Router('repeats', handlers.repeats.repeats_handler, 'List all repeat messages'),
]
