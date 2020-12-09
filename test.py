import ctypes
from ctypes import wintypes
import time, random

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12
VK_CONTROL = 0x11
VK_RIGHT = 0x27
VK_LEFT = 0x25
VK_UP   = 0x26
VK_DOWN = 0x28
VK_LSHIFT = 0xa0
VK_E = 0x45
VK_S = 0x53
VK_X = 0x58
VK_5 = 0x35
VK_3 = 0x33
# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    time.sleep(0.003)

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    time.sleep(0.003)


def randomDelay(min, max):
    time.sleep(random.uniform(min, max))

def ClickKey(hexKeyCode):
    PressKey(hexKeyCode)
    ReleaseKey(hexKeyCode)

def dash(code):
    ClickKey(code)
    #time.sleep(0.1)
    ClickKey(code)

coolTime = dict()
TimeStamp = dict()
coolTime['maha'] = 150
coolTime['brandish'] = 20
coolTime['spider'] = 250
coolTime['sim'] = 210
coolTime['meso'] = 120

TimeStamp['meso'] = 0
TimeStamp['sim'] = 0
TimeStamp['maha'] = 0
TimeStamp['brandish'] = 0
TimeStamp['spider'] = 0

def finalBlow():
    PressKey(VK_DOWN)
    PressKey(VK_CONTROL)
    ReleaseKey(VK_CONTROL)
    ReleaseKey(VK_DOWN)
    randomDelay(0.2, 0.3)

def beyond(n):
    for i in range(n):
        ClickKey(VK_LSHIFT)

def jumpDown():
    PressKey(VK_UP)
    PressKey(VK_DOWN)
    PressKey(VK_MENU)
    PressKey(VK_LEFT)
    time.sleep(0.1)
    ReleaseKey(VK_LEFT)
    ReleaseKey(VK_UP)
    ReleaseKey(VK_MENU)
    ReleaseKey(VK_DOWN)
    time.sleep(0.1)
    finalBlow()
    beyond(1)
    randomDelay(0.8, 0.85)

def jumpUp():
    PressKey(VK_UP)
    PressKey(VK_CONTROL)
    ReleaseKey(VK_CONTROL)
    ReleaseKey(VK_UP)
    time.sleep(0.5)

def jumpLeftDown():
    PressKey(VK_DOWN)
    PressKey(VK_MENU)
    time.sleep(0.1)
    ReleaseKey(VK_MENU)
    ReleaseKey(VK_DOWN)
    time.sleep(0.3)
    dash(VK_LEFT)
    randomDelay(0.75, 0.85)

def jumpLeftUp():
    ClickKey(VK_LEFT)
    PressKey(VK_LEFT)
    time.sleep(0.18)
    PressKey(VK_UP)
    PressKey(VK_CONTROL)
    ReleaseKey(VK_LEFT)
    ReleaseKey(VK_CONTROL)
    ReleaseKey(VK_UP)
    randomDelay(0.35, 0.4)
    ClickKey(VK_UP)
    time.sleep(0.1)
    ClickKey(VK_CONTROL)
    randomDelay(1, 2)

def jumpRightUp():
    ClickKey(VK_S)
    randomDelay(0.1, 0.2)
    ClickKey(VK_UP)
    randomDelay(0.1, 0.2)
    ClickKey(VK_CONTROL)
    randomDelay(0.5, 0.6)

def goLeft():
    ClickKey(VK_LEFT)
    PressKey(VK_LEFT)
    time.sleep(0.18)
    PressKey(VK_UP)
    PressKey(VK_CONTROL)
    ReleaseKey(VK_LEFT)
    ReleaseKey(VK_CONTROL)
    ReleaseKey(VK_UP)
    randomDelay(0.23, 0.25)
    finalBlow()
    beyond(1)
    randomDelay(0.73, 0.74)

def goRight():
    PressKey(VK_RIGHT)
    randomDelay(0.1, 0.2)
    ReleaseKey(VK_RIGHT)
    ClickKey(VK_S)
    randomDelay(0.7, 0.8)
    ClickKey(VK_S)
    randomDelay(0.8, 0.9)
    jumpRightUp()
    for i in range(3):
        ClickKey(VK_S)
        randomDelay(0.7, 0.8)   
    jumpRightUp()
    for i in range(3):
        ClickKey(VK_S)
        randomDelay(0.7, 0.8)  
    

def brandish():
    ClickKey(VK_LEFT)
    PressKey(VK_LEFT)
    time.sleep(0.18)
    PressKey(VK_UP)
    PressKey(VK_CONTROL)
    ReleaseKey(VK_LEFT)
    ReleaseKey(VK_CONTROL)
    ReleaseKey(VK_UP)
    randomDelay(0.2, 0.3)
    dash(VK_DOWN)
    randomDelay(0.2, 0.3)
    ClickKey(VK_CONTROL)
    randomDelay(0.75, 0.85)
    TimeStamp['brandish'] = time.time()

def maha():
    jumpLeftDown()
    ClickKey(VK_E)
    randomDelay(0.2, 0.3)
    dash(VK_UP)
    randomDelay(0.1, 0.2)
    ClickKey(VK_CONTROL)
    randomDelay(0.2, 0.3)
    TimeStamp['maha'] = time.time()

def spider():
    jumpLeftDown()
    ClickKey(VK_X)
    randomDelay(0.2, 0.3)
    TimeStamp['spider'] = time.time()

def case0():
    jumpDown()
    for i in range(4):
        goLeft()
    randomDelay(0.4, 0.5)

def case1():
    jumpDown()
    goLeft()
    goLeft()
    brandish()
    goLeft()
    randomDelay(0.3, 0.5)

def case2():
    maha()
    for i in range(4):
        goLeft()
    randomDelay(0.3, 0.5)

def case3():
    spider()
    for i in range(4):
        goLeft()
    randomDelay(0.3, 0.5)

def case4():
    ClickKey(VK_5)    
    randomDelay(0.5, 0.6)
    case0()
    
def getMeso():
    jumpDown()
    for i in range(3):
        goLeft()
    jumpLeftUp()
    goRight()


def run(running_time=0):
    startTime = time.time()
    mahaOn = False
    while True:
        now = time.time()
        if now - TimeStamp['sim'] > coolTime['sim']:
            ClickKey(VK_3)
            randomDelay(0.6, 0.7)
        if mahaOn:
            case4()
            mahaOn = False
        elif now - TimeStamp['meso'] > coolTime['meso']:
            getMeso()
            TimeStamp['meso'] = time.time()
        elif now - TimeStamp['spider'] > coolTime['spider']:
            case3()
        elif now - TimeStamp['maha'] > coolTime['maha']:
            case2()
            mahaOn = True
        elif now - TimeStamp['brandish'] > coolTime['brandish']:
            case1()
        else:
            case0()

TEST = True
if __name__ == "__main__":
    if TEST:
        time.sleep(1)
        for j in range(10):
            for i in range(15):
                case0()
            getMeso()
    else:
        run()
