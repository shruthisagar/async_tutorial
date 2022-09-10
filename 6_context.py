import asyncio
from contextlib import asynccontextmanager
import aiohttp


"""
A context manager usually takes care of setting up some resource,
e.g. opening a connection, and automatically handles the clean up when we are done with it. 
Probably, the most common use case is opening a file. 
The code above will open the file and will keep it open until we are out of the with statement.
"""

@asynccontextmanager
async def get_client_session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()

async def get_data():
    async with get_client_session() as session:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        result = await session.get(url)
        print (await result.json())
        

if __name__ == '__main__':
    asyncio.run(get_data())
   
