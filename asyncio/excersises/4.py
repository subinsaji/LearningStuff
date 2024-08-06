import aiohttp
import asyncio


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def main():
    url_1 = "https://www.wikipedia.org/"
    url_2 = "https://www.google.com" 
    task_1 = asyncio.create_task(fetch_url(url_1))
    task_2 = asyncio.create_task(fetch_url(url_2))

    data_1 = await task_1
    data_2 = await task_2

    print("Data from ", url_1, len(data_1), "bytes")
    print("Data from ", url_1, len(data_2), "bytes")

asyncio.run(main())

