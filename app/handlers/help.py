from app.handlers.routers import routers


COMMAND_TEXT_FORMAT = "!{command}: {description}"


def help_handler(event):
    help_text = "\n".join([COMMAND_TEXT_FORMAT.format(command=router.command, description=router.description) for router in routers])
    event.respond(help_text)
