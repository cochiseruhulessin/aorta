# pylint: skip-file
import pydantic

from .command import Command
from .command import Ping
from .commandhandler import CommandHandler
from .event import Event
from .eventlistener import EventListener
from .exceptions import *
from .messagehandler import MessageHandler
from .messagepublisher import MessagePublisher
from .messagehandlersprovider import _default
from .messagehandlersprovider import match
from .messagehandlersprovider import parse
from .messagehandlersprovider import register
from .messagehandlersprovider import MessageHandlersProvider
from . import models
from . import transport


def get_default_provider() -> MessageHandlersProvider:
    return _default


def get_models(
    cls: type[Command | Event]
) -> tuple[type[pydantic.BaseModel], type[pydantic.BaseModel]]:
    """Return the envelope and the specification model for a
    class:`Command` or an :class:`Event` implementation.
    """
    return cls.get_models()


__all__ = [
    'match',
    'models',
    'parse',
    'register',
    'transport',
    'Command',
    'CommandHandler',
    'Event',
    'EventListener',
    'MessageHandler',
    'MessageHandlersProvider',
    'MessagePublisher',
    'Ping',
]
