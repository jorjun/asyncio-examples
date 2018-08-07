"""
Demonstrate ThreadPoolExecutor with N worker threads to deal with a blocking function.

@jorjun  Dies Martis, Sol in Leo, Luna in Gemini, An:Viv

"""
import asyncio
import time
import random
import urllib.request
import concurrent.futures
from contextvars import ContextVar

RAND_VARIATION = 5
URL = 'http://xkcd.com'


async def worker_loop(executor, hostid, interval, count):

    def blocking_download_url(url):
        return urllib.request.urlopen(url).read()


    for lcount in range(1, count+1):
        await asyncio.sleep(interval + random.randint(0, RAND_VARIATION))
        result = await loop.run_in_executor(executor, blocking_download_url, URL)
        print(f"Agent: {hostid}, loop: {lcount}, got data len: {len(result)}")

    print(f'Agent: {hostid} finished!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    num_agents = 3
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=num_agents
    ) as executor:
        all_agents = [worker_loop(executor=executor, hostid=hostid, interval=5, count=3)
                      for hostid in range(1, num_agents + 1)]
        loop.run_until_complete(
            asyncio.gather(*all_agents)
        )
        loop.close()
