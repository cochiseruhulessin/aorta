"""Declares :class:`Handler`."""
import typing

from .models import Message


class Handler:
    """Handles an incoming message using the :meth:`handle()` method."""

    #: A list of tuples specifying the api version and message type
    #: that are accepted by this handler.
    handles: typing.List[typing.Tuple[str, str]] = []

    def can_handle(self, message: Message) -> bool:
        """Return a boolean indicating if the :class:`Handler` knows
        how to process `message`.
        """
        return (message.api_version, message.kind) in self.handles

    async def handle(self, message: Message, *args, **kwargs):
        """Invokes for each incoming message that matches the handlers'
        criteria.
        """
        raise NotImplementedError
