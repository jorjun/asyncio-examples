""" Simple mutually-recursive coroutines with asyncio. Note that these recursive calls
continue to grow the stack (and will eventually hit the maximum recursion depth
exception if too many recursive calls are made. """

import asyncio

async def a(n):
    print("A: {}".format(n))
    if n > 10: return n
    else: await b(n+1)

async def b(n):
    print("B: {}".format(n))
    await a(n+1)

loop = asyncio.get_event_loop()
loop.run_until_complete(a(0))

