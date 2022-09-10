import asyncio
from time import perf_counter
import requests
import aiohttp
url = "https://jsonplaceholder.typicode.com/posts/{}"

users = []
def get_user_sync(user_id:int) -> dict:
    user = requests.get(url.format(user_id))
    return user.json().get("title", "No Title")

async def get_user_async(user_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        user = await session.get(url.format(user_id))
        user = await user.json()
        return user.get("title", "No Title")

async def main():
    time_start = perf_counter()
    await asyncio.gather(*[get_user_async(i) for i in range(40)])
    print(f"ASync =  {perf_counter()-time_start}")
    
    time_start = perf_counter()
    
    [get_user_sync(i) for i in range(40)]    
    print(f"sync =  {perf_counter()-time_start}")
    

if __name__ ==  "__main__":
    asyncio.run(main())
    