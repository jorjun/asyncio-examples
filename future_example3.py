# This doesn't actually explicitly use a Future, but shows how to get the same
# behavior with just coroutines.

import asyncio

async def slow_operation():
    await asyncio.sleep(1)
    return 42

async def call_slow_operation():
    result = await slow_operation()
    print("The answer is: {}".format(result))

loop = asyncio.get_event_loop()
loop.run_until_complete(call_slow_operation())
loop.close()

