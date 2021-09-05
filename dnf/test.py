import pywinio
import time
import atexit
import win32com.client
import win32gui
import win32process
import win32api
import win32con


def person_locate(dm):
    # 人物坐标计算
    dm_ret = None
    num = 0
    while 1:
        dm_ret = dm.FindStrFast(0, 0, 1920, 1080, "lv2", "d9d9d9-505050", 0.9)
        if dm_ret[1] != -1:
            break
        else:
            num += 1
            print('计算当前人物坐标', num)
            time.sleep(1)
    dm = win32com.client.Dispatch('dm.dmsoft')
    # 返回人物坐标 x = dm_ret[1] y = dm_ret[2]
    return dm_ret[1], dm_ret[2], dm


def move():
    # x轴速度 217 y轴速度 281
    pass


def dnf_run():
    # 运行前
    dm = win32com.client.Dispatch('dm.dmsoft')
    whandle = win32gui.FindWindow(None, '地下城与勇士')
    state = dm.SetKeypadDelay('windows', 1000)
    dm.SetWindowState(whandle, 1)
    dm.SetPath(r'D:\python_code\pydamo\接口说明')
    dm.SetDict(0, "yunjisuan.txt")

    time.sleep(2)
    dm.MoveTo(1000, 0)
    dm.LeftClick()
    time.sleep(2)
    # dm.KeyDown(39)
    # dm.KeyUp(39)
    x1, y1, dm = person_locate(dm)
    print('1', x1, y1)
    # time.sleep(1)
    dm.KeyDown(37)
    time.sleep(1)
    dm.KeyUp(37)
    time.sleep(2)
    dm.KeyDown(38)
    time.sleep(1)
    dm.KeyUp(38)
    # # # 人物 70 高度和物品
    x2, y2, dm = person_locate(dm)
    print('2', x2, y2)
    speed_x = (x1 - x2)
    speed_y = (y1 - y2)
    print('3', speed_x, speed_y)

    # print(2)
    # status = dm.BindWindowEx(whandle, 'normal', 'dx.mouse.position.lock.api', "dx.keypad.input.lock.api", "dx.public.active.api", 0)
    # 绑定窗口目前失败
    # print('bind')
    # try:
    #     status = dm.BindWindow(whandle, 'gdi', 'dx', 'dx', 0)
    #     print(status)
    # except Exception as e:
    #     print(dm.GetLastError())
    #     print(e)


    # 运行后
    # 解除绑定

    # 如何寻路 -- 速度 时间 路程


def shuatu():
    '''
    1.得到现在所处的坐标
    2.按指定的移动键，固定时间，再释放
    3.重新取得人物坐标
    4.现在人物坐标- 之前坐标 = 路程

    大漠工具将运行目录置全局 -- 提取特征字库文件
    大漠工具设置字库_置文件
    大漠 找字 --
    '''
    dm = win32com.client.Dispatch('dm.dmsoft')
    # whandle = win32gui.FindWindow(None, '地下城与勇士')
    # dm_ret = dm.SetWindowState(whandle, 1)
    dm_ret = dm.SetDict(0, "dm_soft.txt")
    print(dm_ret)
    time.sleep(2)
    # 需要新建文件代表字库 使用默认文件报错 --
    dm_ret = dm.FindStr(0, 0, 1280, 720, "淡忘", "bea74c-000000", 0.9)
    print(dm_ret)

# shuatu()

dnf_run()
# import os
# time.sleep(3)
# # dnf_run()
# # shuatu()
# dm = win32com.client.Dispatch('dm.dmsoft')
# dm_ret = dm.SetPath(r'D:\python_code\pydamo\接口说明')
# print(os.getcwd())
# dm_ret = dm.SetDict(0, "yunjisuan.txt")
# print(dm_ret)
# time.sleep(2)
# dm_ret = dm.FindStrFast(0, 0, 1920, 1080, "云计算", "dcffff-808080", 0.9)
# print(dm_ret)