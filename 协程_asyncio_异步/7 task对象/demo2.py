import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def main():
    print("main start")
    task_list = [
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2')
    ]
    print("main end")
    # 任务执行
    done, pending = await asyncio.wait(task_list)
    print(done)


asyncio.run(main())