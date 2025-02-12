from app.handlers.routers import routers


COMMAND_TEXT_FORMAT = "{command}: {description}\n```{command_with_example_args}```"


async def help_handler(event):
    help_text = "\n".join([COMMAND_TEXT_FORMAT.format(
        command=router.command,
        description=router.description,
        command_with_example_args=f"!{router.command} {router.example_args}".strip() if router.example_args is not None else ""
    ).strip() for router in routers])
    await event.respond(help_text)
