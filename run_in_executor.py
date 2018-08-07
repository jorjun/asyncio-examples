import asyncio
from urllib.request import urlopen


async def print_data_size():
   data = await get_data_size()
   print(f"Data size: {data['data1']} + {data['data2']} = { data['data1'] + data['data2'] }")

# Note that this is a synchronous function
def sync_get_url(url):
   return urlopen(url).read()


async def get_data_size():
   loop = asyncio.get_event_loop()

   # These each run in their own thread (in parallel)
   future1 = loop.run_in_executor(None, sync_get_url, 'http://xkcd.com')
   future2 = loop.run_in_executor(None, sync_get_url, 'http://google.com')

   # While the synchronous code above is running in other threads, the event loop
   # can go do other things.
   data1 = await future1
   data2 = await future2
   return {
      "data1": len(data1),
      "data2": len(data2),
   }

loop = asyncio.get_event_loop()
loop.run_until_complete(print_data_size())

