import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"Started at {time.strftime('%X')}")
    await say_after(1, 'Hello')
    await say_after(2, "World")
    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())
