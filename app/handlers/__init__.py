from telethon import events

from app.handlers import routers
from app.telegram_client import client


def setup_routers():
    client.on(events.NewMessage(pattern='!ping', outgoing=True))(routers.ping_handler)
    client.on(events.NewMessage(pattern='!id', outgoing=True))(routers.id_handler)
    client.on(events.NewMessage(pattern='!delete_all_goals', outgoing=True))(routers.delete_all_goal_handler)
    client.on(events.NewMessage(pattern='!new_goal', outgoing=True))(routers.new_goal_handler)
    client.on(events.NewMessage(pattern='!goals', outgoing=True))(routers.goals_handler)
    client.on(events.NewMessage(pattern='!force_new_goal', outgoing=True))(routers.force_new_goal_handler)
