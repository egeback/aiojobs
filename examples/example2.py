import asyncio

import aiojobs


async def coro(timeout):
    await asyncio.sleep(timeout)


async def main():
    scheduler = await aiojobs.create_scheduler()
    for i in range(10):
        # spawn jobs
        scheduler.sync_spawn(coro(i/10))

    await asyncio.sleep(5.0)
    # not all scheduled jobs are finished at the moment

    # gracefully close spawned jobs
    await scheduler.close()

asyncio.get_event_loop().run_until_complete(main())
print("done")
