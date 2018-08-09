import asyncio

# Tail-recursive factorial using asyncio event loop as a trampoline to
# keep the stack from growing.


async def factorial(n, callback, acc=1):
    if n == 0:
        callback(acc)
    else:
        print(f"factorial {n}-1, {callback}, {acc}*{n})")
        asyncio.ensure_future(factorial(n-1, callback, acc*n))

def done_callback(result):
    print("Result: {}".format(result))
    loop = asyncio.get_event_loop()
    loop.stop()


loop = asyncio.get_event_loop()
asyncio.ensure_future(
    factorial(50000, done_callback)
)
loop.run_forever() # Blocking call interrupted by loop.stop()
loop.close()

