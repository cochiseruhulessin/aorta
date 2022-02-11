"""Declares :class:`EventPublisher`."""
import typing
import uuid

from unimatrix.lib import timezone

from .models import Message
from .sender import Sender
from .transport import ITransport


class EventPublisher(Sender):
    """Provides an interface to published event messages."""
    __module__: str = 'aorta'

    async def publish(self,
        dto: typing.Union[dict, Message],
        correlation_id: str = None
    ):
        """Publish an event to the upstream peer."""
        if not isinstance(dto, Message):
            dto['type'] = "unimatrixone.io/event"
            dto = self.prepare(dto, correlation_id=correlation_id)
        await self.send(dto)
