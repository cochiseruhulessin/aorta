from typing import overload

from .command import Command
from .event import Event


class MessageHandler:
    handles: list[type[Command] | type[Event]]

    @overload
    async def handle(self, command: Command) -> None:
        ...

    @overload
    async def handle(self, event: Event) -> None:
        ...