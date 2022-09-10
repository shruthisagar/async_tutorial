import asyncio

async def main():
    print("statement 1")
    await asyncio.sleep(1)
    print("statement 2")
    
if __name__ == "__main__":
    asyncio.run(main())