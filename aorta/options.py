"""Declares :class:`Options`."""


class Options:
    """Configures an event listener or command handler."""

    def __init__(self, meta: object):
        self.handles = getattr(meta, 'handles', [])
