import pywinio
import time
import atexit
import win32com.client
import win32gui
import win32process
import win32api



# 键值表：https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
# https://blog.csdn.net/deniece1/article/details/103588428?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0.control&spm=1001.2101.3001.4242

# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

g_winio = None


key_alpha = {
    # 字母表
    'q': 0x10,
    'w': 0x11,
    'e': 0x12,
    'r': 0x13,
    't': 0x14,
    'y': 0x15,
    'u': 0x16,
    'i': 0x17,
    'o': 0x18,
    'p': 0x19,
    'a': 0x1e,
    's': 0x1f,
    'd': 0x20,
    'f': 0x21,
    'g': 0x22,
    'h': 0x23,
    'j': 0x24,
    'k': 0x25,
    'l': 0x26,
    'z': 0x2c,
    'x': 0x2d,
    'c': 0x2e,
    'v': 0x2f,
    'b': 0x30,
    'n': 0x31,
    'm': 0x32}
key_beta = {
    # 数字表
    '0': 0x0b,
    '1': 0x02,
    '2': 0x03,
    '3': 0x04,
    '4': 0x05,
    '5': 0x06,
    '6': 0x07,
    '7': 0x08,
    '8': 0x09,
    '9': 0x0a,
}

key_gamma = {
    'Enter': 0x0a,
    'Space': 0x0a,
    'Esc': 0x01,
    'F1': 0x3b,
    'F2': 0x3c,
    'F3': 0x3d,
    'F4': 0x3e,
    'F5': 0x3f,
    'F6': 0x40,
    'F7': 0x41,
    'F8': 0x42,
    'F9': 0x43,
    'F10': 0x44,
    'F11': 0x45,
    'F12': 0x46,
    'Up': 0x48,
    'Down': 0x50,
    'Left': 0x4b,
    'Right': 0x4d,
}

def get_winio():
    global g_winio
    if g_winio is None:
            g_winio = pywinio.WinIO()
            def __clear_winio():
                    global g_winio
                    g_winio = None
            atexit.register(__clear_winio)
    return g_winio


def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''
    winio = get_winio()
    dwRegVal = 0x02
    while (dwRegVal & 0x02):
            dwRegVal = winio.get_port_byte(KBC_KEY_CMD)


def key_down(scancode):
    winio = get_winio()
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode)


def key_up(scancode):
    winio = get_winio()
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode | 0x80)


def key_press(scancode, press_time=0.2):
    key_down(scancode)
    time.sleep(press_time)
    key_up(scancode)

def dnf_run():
    # 运行前
    dm = win32com.client.Dispatch('dm.dmsoft')
    whandle = win32gui.FindWindow(None, '地下城与勇士')
    print(whandle)
    dm_ret = dm.SetWindowState(whandle, 1)
    time.sleep(2)
    print(2)
    # status = dm.BindWindowEx(whandle, 'normal', 'dx.mouse.position.lock.api', "dx.keypad.input.lock.api", "dx.public.active.api", 0)
    # 绑定窗口目前失败
    # try:
    #     status = dm.BindWindowEx(whandle, 'normal', 'normal', "normal", "dx.public.active.api", 0)
    # except Exception as e:
    #     print(e)


    time.sleep(2)
    dm.KeyDownChar('right')
    time.sleep(2)
    dm.KeyDownChar('left')

    # 运行后
    # 解除绑定

time.sleep(3)
dnf_run()