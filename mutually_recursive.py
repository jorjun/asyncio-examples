""" Simple mutually-recursive coroutines with asyncio. Using asyncio.ensure_future
instead of yield from allows the coroutine to exit and merely schedules the next
call with the event loop, allowing infinite mutual recursion. """

import asyncio

async def a(n):
    print("A: {}".format(n))
    asyncio.ensure_future(b(n+1))

async def b(n):
    print("B: {}".format(n))
    asyncio.ensure_future(a(n+1))

loop = asyncio.get_event_loop()
asyncio.ensure_future(a(0))
loop.run_forever()
loop.close()
