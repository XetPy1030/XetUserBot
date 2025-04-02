from telethon import events

from app.handlers import routers
from app.handlers.help import help_handler
from app.handlers.message import reaction_handler
from app.telegram_client import client


def setup_routers():
    for router in routers.routers:
        client.on(events.NewMessage(pattern=f'!{router.command}($| )', outgoing=True))(router.handler)

    client.on(events.NewMessage(pattern='!help($| )', outgoing=True))(help_handler)
    
    client.on(events.NewMessage(outgoing=False))(reaction_handler)
