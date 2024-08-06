import asyncio
import time

async def task1():
    print("task 1 started")
    await asyncio.sleep(1)
    print("task 1 completed")

async def task2():
    print("task 2 started")
    await asyncio.sleep(6)
    print("task 2 completed")


async def task3():
    print("task 3 started")
    await asyncio.sleep(0)
    print("task 3 completed")

async def task4():
    print("task 4 started")
    await asyncio.sleep(1)
    print("task 4 completed")

async def main():
    start_time = time.time()
    await asyncio.gather(task1(), 
                   task2(), 
                   task3(), 
                   task4()
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nAll tasks completed in {:.2f} seconds".format(elapsed_time))

asyncio.run(main())




