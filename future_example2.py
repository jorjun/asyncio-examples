import asyncio

async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result(42)

async def call_slow_operation():
    def future_callback(future):
        result = fut.result()
        print("The answer is: {}".format(result))

    fut = asyncio.Future()
    fut.add_done_callback(future_callback)
    await slow_operation(fut)

asyncio.run(call_slow_operation())

