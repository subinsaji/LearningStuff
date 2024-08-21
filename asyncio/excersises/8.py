import asyncio
import random

async def producer(queue, id):
    for i in range(3):
        item = f"item: {id}-{i}"
        await queue.put(item)
        print(f"Producer {id} produced -> {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))
    

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"consumer consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue, i)) for i in range(3)]
    consumer_tasks = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.join()
    await queue.put(None)
    await consumer_tasks


asyncio.run(main())




