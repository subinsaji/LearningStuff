import aiohttp
import asyncio


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

url = [ "https://www.wikipedia.org/",
       "https://www.google.com",
       "https://www.facebook.com",
       "https://www.linkedin.com",
       "https://www.x.com",
       "https://www.paypal.com"

]

async def main():
    tasks = asyncio.create_task(fetch_url(url))
    data_1 = await tasks
    print("Data from ", url, len(data_1), "bytes")

asyncio.run(main())

