"""Declares :class:`MessageMetadata`."""
import uuid

import pydantic
from unimatrix.lib import timezone


class MessageMetadata(pydantic.BaseModel):
    message_id: uuid.UUID = pydantic.Field(
        alias='messageId',
        default_factory=uuid.uuid4
    )

    correlation_id: uuid.UUID = pydantic.Field(
        alias='correlationId',
        default_factory=uuid.uuid4
    )

    published: int = pydantic.Field(
        default_factory=timezone.now
    )

    annotations: dict = pydantic.Field({})
    labels: dict = pydantic.Field({})
