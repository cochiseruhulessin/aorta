"""Declares :class:`EventListener`."""
import typing

from .handler import Handler
from .models import Message


class EventListener(Handler):
    """A :class:`Handler` implementation that processes messages that
    represent events.
    """
    __module__: str = 'aorta'
