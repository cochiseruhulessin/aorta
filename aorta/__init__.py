# pylint: skip-file
import ioc

from .commandissuer import CommandIssuer
from .commandhandler import CommandHandler
from .dispatcher import Dispatcher
from .eventlistener import EventListener
from .eventpublisher import EventPublisher
from .handler import Handler
from .handlersprovider import HandlersProvider
from .runner import BaseRunner
from .runner import FastAPIRunner
from . import models
from . import transport


__all__ = [
    'models',
    'publish',
    'transport',
    'BaseRunner',
    'CommandHandler',
    'Dispatcher',
    'EventListener',
    'EventPublisher',
    'FastAPIRunner',
    'Handler',
    'HandlersProvider',
]


_issuer = ioc.require('CommandIssuer')
_provider = HandlersProvider()
_publisher = ioc.require('EventPublisher')


async def issue(name: str, params: dict, version: str = 'v1') -> None:
    """Issue a command using the default command issuer."""
    await _issuer.issue({
        'apiVersion': version,
        'kind': name,
        'spec': params
    })


async def publish(name: str, params: dict, version: str = 'v1') -> None:
    """Publishes an event using the default event publisher."""
    await _publisher.publish({
        'apiVersion': version,
        'kind': name,
        'data': params
    })


def register(*args, **kwargs):
    return _provider.register(*args, **kwargs)
register.__doc__ = _provider.register.__doc__
