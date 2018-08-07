"""
Demonstrate async 'gather' vs 'as_completed'

@jorjun Dies Martis, Sol in Leo, Luna in Gemini, An:Viv
"""
import asyncio

async def waitn(n):
    await asyncio.sleep(n)
    return f"I waited {n}"

async def task_gathered():
    # Results will be delivered in order of call
    results = await asyncio.gather(
        waitn(3), waitn(0), waitn(1)
    )
    print(f"Gathered: {results}")


async def task_as_complete():
    tasks = [waitn(i) for i in (3, 0, 1)]
    for result in  asyncio.as_completed(tasks):
        print(f"As completed: {await result}")

loop = asyncio.get_event_loop()
print("First gathered results:-", end="\n\n")
loop.run_until_complete(task_gathered())
print("-" * 60)
print("Now as-completed results:-", end="\n\n")
loop.run_until_complete(task_as_complete())
print("-- END --")
loop.close()
