"""Declares :class:`Message`."""
import pydantic


class Message(pydantic.BaseModel):
    api_version: str = pydantic.Field(..., alias='apiVersion')
    kind: str = pydantic.Field(...)
    type: str = pydantic.Field(None)
    data: dict = pydantic.Field({})
    spec: dict = pydantic.Field({})
