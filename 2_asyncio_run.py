# Running a program indefintely or for the time we specify it to stop
import asyncio
from datetime import datetime

def print_now():
    print(datetime.now())

async def keep_printing(key_word:str = "")->None:
    while True:
        print(key_word, end="")
        print_now()
        # await is used to block
        # allows asyncio to do something else till 0.50 seconds are over.
        # it yields function that runs later
        await asyncio.sleep(0.50)

async def async_main()-> None:
    # a main function that handles all the async functions in our program
    kp = keep_printing("Time is ")
    waiter = await asyncio.wait_for(kp, 5)
    try:
        await waiter
    except asyncio.TimeoutError:
        print("time's up!")
    
if __name__ == "__main__":
    # asyncio.run(keep_printing())
    # wait for execution to complete or exit after 10 seconds 
    # asyncio.run(asyncio.wait_for(keep_printing(), 10))
    asyncio.run(async_main())