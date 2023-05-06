import asyncio

async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_numbers())
    await task1
    await task2

asyncio.run(main())
