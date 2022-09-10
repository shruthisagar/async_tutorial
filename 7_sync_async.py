import asyncio
from time import sleep

async def a_function():
    await asyncio.sleep(1)
    print("async hello")

def another_function():
    sleep(1)
    print("sync hello")

async def do_stuff():
    await a_function()
    another_function()

async def main():
    tasks = []
    for _ in range(3):
        tasks.append(asyncio.create_task(do_stuff()))
    await asyncio.gather(*tasks)

asyncio.run(main())