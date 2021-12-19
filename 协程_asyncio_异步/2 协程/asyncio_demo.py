import asyncio

@asyncio.coroutine # 协程函数
def func1():
    print(1)
    # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    # 遇到IO阻塞自动切换，sleep的时候切换到其他任务
    yield from asyncio.sleep(2)
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    yield from asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))