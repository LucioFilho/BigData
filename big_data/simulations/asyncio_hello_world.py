import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # Run two say_after tasks concurrently:
    await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world'),
    )

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

'''perform asynchronous operations concurrently, 
making it possible to run multiple I/O-bound tasks 
more efficiently than running them sequentially'''