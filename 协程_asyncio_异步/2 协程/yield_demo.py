def func1():
    yield 1
    # 跳到func2执行，执行完回来打印2
    yield from func2()
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    print(item)