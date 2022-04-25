import asyncio
import time


# Using asyncio.create_task() function to run coroutines concurrently
# as asyncio Tasks
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(1, 'Hello'))
    task2 = asyncio.create_task(say_after(2, 'World'))

    print(f"Started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take around 2 seconds)
    await task1
    await task2

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())