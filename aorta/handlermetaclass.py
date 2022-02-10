"""Declares :class:`HandlerMetaclass`."""
from .options import Options


class HandlerMetaclass(type):

    def __new__(cls, name, bases, attrs):
        new = super().__new__
        if name in ('Handler', 'CommandHandler', 'EventListener'):
            return new(cls, name, bases, attrs)
        meta = attrs.pop('Meta', None)
        if meta is None:
            raise AttributeError(
                f"Declare an inner Meta class for {name}"
            )
        attrs['_meta'] = Options(meta)
        return new(cls, name, bases, attrs)
