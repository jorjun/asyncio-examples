"""
Download web pages in parallel, count how many times a specified
word is used in each of them. And time taken.
"""

import asyncio
import aiohttp

async def download_and_count_word(word, url):
    t_start = loop.time()
    async with aiohttp.request('GET', url) as response:
        text = await response.read()
        return {
            "dur_s": (loop.time() - t_start),
            "url": url,
            "count": text.decode().lower().count(word)
        }


async def count_word_in_pages(word, urls):
    for done in asyncio.as_completed(
        [download_and_count_word(word, url) for url in urls]
    ):
        data = await done
        print(f"{word!r} appears {data['count']} times in {data['url']}. ({data['dur_s']:.2} seconds)")

word = "will"
urls = ["http://calebmadrigal.com",
         "http://yahoo.com",
         "http://xkcd.com",
         "http://reddit.com",
         "http://news.ycombinator.com",
         "https://nuyidao.com/about/"]

loop = asyncio.get_event_loop()
loop.run_until_complete(count_word_in_pages(word, urls))
loop.close()

