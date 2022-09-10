import asyncio


async def example_coroutine_function():
    print("I am in a function")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
t = loop.create_task(example_coroutine_function())
r = loop.run_until_complete(t)