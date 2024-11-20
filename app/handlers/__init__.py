from telethon import events

from app.handlers import routers
from app.telegram_client import client


def setup_routers():
    client.on(events.NewMessage(pattern='/id'))(routers.id_handler)
    client.on(events.NewMessage(pattern='/delete_all_goal'))(routers.delete_all_goal_handler)
    client.on(events.NewMessage(pattern='/new_goal'))(routers.new_goal_handler)
    client.on(events.NewMessage(pattern='/goals'))(routers.goals_handler)
    client.on(events.NewMessage(pattern='/force_new_goal'))(routers.force_new_goal_handler)
