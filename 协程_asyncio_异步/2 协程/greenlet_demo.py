# 实现协程方法
from greenlet import greenlet


def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()


def func2():
    print(3)
    gr1.switch()
    print(4)
    gr1.switch()


gr1 = greenlet(func1)
gr2 = greenlet(func2)
# 不停进行切换 通过switch切换执行
gr1.switch()