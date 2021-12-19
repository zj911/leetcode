import asyncio
# async关键字取代装饰器


async def func1():
    print(1)
    # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    # 遇到IO阻塞自动切换，sleep的时候切换到其他任务
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
