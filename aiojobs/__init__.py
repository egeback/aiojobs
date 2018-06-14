"""Jobs scheduler for managing background task (asyncio).

The library gives controlled way for scheduling background tasks for
asyncio applications.

"""


__version__ = '0.2.2_me'

import asyncio
from ._scheduler import Scheduler


# Added typing
def sync_create_scheduler(*, loop=None, close_timeout=0.1, limit=100,
                          pending_limit=10000, exception_handler=None) -> Scheduler:
    if exception_handler is not None and not callable(exception_handler):
        raise TypeError('A callable object or None is expected, '
                        'got {!r}'.format(exception_handler))

    loop = loop or asyncio.get_event_loop()
    return Scheduler(loop=loop, close_timeout=close_timeout,
                     limit=limit, pending_limit=pending_limit,
                     exception_handler=exception_handler)


# Added typing
async def create_scheduler(*, loop=None, close_timeout=0.1, limit=100,
                           pending_limit=10000, exception_handler=None) -> Scheduler:
    return sync_create_scheduler(loop=loop, close_timeout=close_timeout, limit=limit, pending_limit=pending_limit,
                                 exception_handler=exception_handler)

__all__ = ('create_scheduler', 'sync_create_scheduler',)
