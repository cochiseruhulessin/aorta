"""Declares :class:`Message`."""
import pydantic

from .messagemetadata import MessageMetadata


class Message(pydantic.BaseModel):
    api_version: str = pydantic.Field(..., alias='apiVersion')
    kind: str = pydantic.Field(...)
    type: str = pydantic.Field(None)
    metadata: MessageMetadata = pydantic.Field(...)
    data: dict = pydantic.Field({})
    spec: dict = pydantic.Field({})

    @property
    def qualname(self) -> tuple:
        """Return the qualified name of the message type."""
        return (self.api_version, self.kind)

    def is_command(self) -> bool:
        """Return a boolean indicating if the message is a command."""
        return self.type == "unimatrixone.io/command"

    def is_event(self) -> bool:
        """Return a boolean indicating if the message is an event."""
        return self.type == "unimatrixone.io/event"
