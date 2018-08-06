import asyncio

async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result(42)

async def call_slow_operation():
    fut = asyncio.Future()
    await slow_operation(fut)
    result = fut.result()
    print("The answer is: {}".format(result))

loop = asyncio.get_event_loop()
loop.run_until_complete(call_slow_operation())
loop.close()

