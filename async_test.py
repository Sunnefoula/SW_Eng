import asyncio


async def sleep_a_little(time_to_sleep):
    await asyncio.sleep(1)  # pauses 1sec


async def go_do_smth():
    time_to_sleep = 1
    await sleep_a_little(time_to_sleep)


asyncio.run(go_do_smth())
# uvicorn takes care of async functions without the use of asyncio module