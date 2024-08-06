import asyncio
import random

async def time_consuming_task():
    print("starting time consuming task")
    try:
        for i in range(1,10):
            await asyncio.sleep(random.randint(6,10))
            print(f"step {i} completeted")
    except asyncio.CancelledError:
        print("Time consuming task was cancelled")
        raise

async def main():
    task = asyncio.create_task(time_consuming_task())
    await asyncio.sleep(random.randint(1,8))
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Main coroutine caught task cancellation!")

asyncio.run(main())


