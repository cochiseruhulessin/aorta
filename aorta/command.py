"""Declares :class:`Command`."""
from typing import NoReturn

from .basemessage import BaseMessage
from .messagemetaclass import MessageMetaclass
from .types import RetryCommand


class CommandMetaclass(MessageMetaclass):
    envelope_field: str = 'spec'
    message_type: str = 'unimatrixone.io/command'


class Command(BaseMessage, metaclass=CommandMetaclass):
    """The parameters for a :term:`Command`."""
    __abstract__: bool = True

    def retry(self) -> NoReturn:
        """Indicates to the runner that the command must be retried."""
        raise RetryCommand


class Ping(Command):
    """Indicates a ping to an application."""