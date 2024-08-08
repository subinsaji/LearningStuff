import asyncio

async def one_second_delay():
    await asyncio.sleep(1)
    print ("once second delay")

async def two_second_delay():
    await asyncio.sleep(2)
    print ("two second delay")

async def three_second_delay():
    await asyncio.sleep(3)
    print ("three second delay")

async def main():
    await one_second_delay()
    await two_second_delay()
    await three_second_delay()


asyncio.run(main())

#very DRY approach