from app.handlers.routers import routers, Router

COMMAND_TEXT_FORMAT = "{command}: {description}"


async def help_handler(event):
    await event.respond(get_help_text())


def get_help_text():
    help_text = "\n".join(
        [COMMAND_TEXT_FORMAT.format(
            command=router.command,
            description=get_description(router),
        ).strip() for router in routers]
    )
    return help_text


def get_description(router: Router) -> str:
    description = router.description
    if router.example_args is not None:
        command_with_example_args = f"!{router.command} {router.example_args}".strip()
        description = f"{description}\n```{command_with_example_args}```"
    return description


print(get_help_text())
