import asyncio

async def display_name_and_delay(name, delay):
    await asyncio.sleep(delay)
    print(name)

async def main():
    tasks = [
        display_name_and_delay("one second delay", 1),
        display_name_and_delay("two second delay", 2),
        display_name_and_delay("three second delay", 3)
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())