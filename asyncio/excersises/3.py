import asyncio

async def print_numbers_with_delay():
    for i in range (1,8):
        print(i)
        await asyncio.sleep(1)

# make event loop

asyncio.run(print_numbers_with_delay())
