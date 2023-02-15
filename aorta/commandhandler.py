"""Declares :class:`CommandHandler`."""
from typing import NoReturn

from .commandhandlermetaclass import CommandHandlerMetaclass
from .messagehandler import MessageHandler
from .types import RetryCommand


class CommandHandler(MessageHandler, metaclass=CommandHandlerMetaclass):
    """Handles command messages."""
    __abstract__: bool = True
    __module__: str = 'aorta'


    def retry(self) -> NoReturn:
        """Indicates to the runner that the command must be retried."""
        raise RetryCommand