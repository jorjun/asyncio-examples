"""
Demonstrate use of concurrent.futures.ThreadPoolExecutor (default executor: None, already in the event loop)
to bring good asynchronous behaviour to a non-asyncio, blocking function.
Show how each task is 'gathered' until completion.

@jorjun  Dies Martis, Sol in Leo, Luna in Gemini, An:Viv
"""
import asyncio
import time
from urllib.request import urlopen
from functools import partial


def blocking_get_page_len(url):
    time.sleep(2) # This is the blocking sleep (not the async-friendly one)
    page = urlopen(url).read()
    return len(page)

async def task_count_to_10():
    for i in range(11):
        print(f"Counter: {i}")
        await asyncio.sleep(.5)


async def task_print_data_size():
    data = await loop.run_in_executor(
        None,  partial(blocking_get_page_len, url="http://calebmadrigal.com")
    )
    print(f"Data size: {data}")


loop = asyncio.get_event_loop()
loop.set_debug(True)

tasks = [
    task_count_to_10(),
    task_print_data_size()
]

loop.run_until_complete(
    asyncio.gather(*tasks)
)
loop.close()

