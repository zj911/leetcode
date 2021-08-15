# 关于python调用大漠插件的示例
import ctypes
# ctype可调用dll库
import win32gui
import win32process
import win32api
import win32com.client
import time

# windows api
# 大漠插件api
# pywin32 api

# 获取窗口句柄
# whandle = win32gui.FindWindow(None, '地下城与勇士')
# print(hex(whandle))

# 获取进程pid
# pid = win32process.GetWindowThreadProcessId(whandle)
# print(pid)

# 获取进程句柄
# phandle = win32api.OpenProcess((0x1F0FFF, False, pid))
# print(whandle)

# 远程进程exe内容基址
# ret = win32process.EnumProcessModules(phandle)
# print(ret[0])

def memory_update():
    # 读取内存。基址 + 偏移 例子：E20710, kernel32
    kernel32 = ctypes.windll.LoadLibrary('c:\Windows\system32\kernel32.dll')
    data = ctypes.c_long()
    kernel32.ReadProcessMemory(phandle, ret[0] + 0xE20710, ctypes.byref(data), 4, None)
    print(data.value)

    # 读取到内存的数值，CE可修改查看
    import win32com.client
    # 大漠插件修改内存
    dm = win32com.client.Dispatch('dm.dmsoft')

    # 第一次查找的内存地址范围
    fanwei = str(ret[0])+'-0x7ffffffffff'
    list1 = dm.FindInt(whandle, fanwei, data.value, data.value, 0)
    list2 = []
    while True:
        data1 = data.value
        data2 = ctypes.c_long()
        kernel32.ReadProcessMemory(phandle, ret[0] + 0xE20710, ctypes.byref(data2), 4, None)
        data2 = data2.value
        if data1 != data2:
            # 查找到目标地址后更新当前地址并且break
            list2 = dm.FindInt(whandle, fanwei, data2, data2, 0)
            break
    # 返回目标内存地址
    list2 = list2.split('|')
    print(list2)

    if len(list2) < 5 and len(list2) > 0:
        for num in list2:
            # unocde > 16进制
            num = int(num, 16)
            # 写入内存成功
            kernel32.WriteProcessMemory(phandle, num, ctypes.byref(ctypes.c_long(66666)), 4, None)


def get_hwnd():
    # 返回整型表示的窗口句柄
    dm = win32com.client.Dispatch('dm.dmsoft')
    # 获取当前鼠标指向窗口句柄
    hwnd = dm.GetMousePointWindow()
    # 获取类名窗口句柄
    whandle = win32gui.FindWindow(None, '地下城与勇士')
    print(hex(whandle))

