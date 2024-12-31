from telethon import events

import app.handlers.common
import app.handlers.goals
import app.handlers.repeats
import app.handlers.schedules
from app.handlers import routers
from app.handlers.help import help_handler
from app.telegram_client import client


def setup_routers():
    for router in routers.routers:
        client.on(events.NewMessage(pattern=f'!{router.command}', outgoing=True))(router.handler)

    client.on(events.NewMessage(pattern='!help', outgoing=True))(help_handler)
