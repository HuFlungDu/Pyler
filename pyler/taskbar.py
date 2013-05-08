from pyler import window

import win32gui
import ctypes
import time
# We only need to import one of these. For some inexplicable reason, you need to import one of these for
# ctypes.wintypes to work. I really don't know why
from ctypes.wintypes import DWORD

class APPBARDATA(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.wintypes.DWORD),
                    ("hWnd", ctypes.wintypes.HANDLE),
                    ("uCallbackMessage", ctypes.wintypes.UINT),
                    ("uEdge", ctypes.wintypes.UINT),
                    ("rc", ctypes.wintypes.RECT),
                    ("lParam", ctypes.wintypes.LPARAM)]

class Taskbar(object):
    def __init__(self):
        self.taskbar = window.find_window("Shell_TrayWnd")
        desktop = win32gui.GetDesktopWindow()
        self.start_button = window.Window(win32gui.FindWindowEx(desktop
                ,None
                ,"button"
                , None
            ))

        self.appbarData = APPBARDATA(ctypes.sizeof(APPBARDATA)
                ,self.taskbar.get_window()
                ,0
                ,0
                ,ctypes.wintypes.RECT(0,0,0,0)
                ,0
        )

    def hide(self):
        self.taskbar.hide()
        self.start_button.hide()
        #self.set_auto_hide(True)
        pass

    def show(self):
        self.taskbar.show()
        self.start_button.show()
        #self.set_auto_hide(False)

    def set_auto_hide(self,autohide):
        start = time.time()
        self.appbarData.lParam = int(autohide)
        ctypes.windll.shell32.SHAppBarMessage(10
                , ctypes.byref(self.appbarData)
        )
        print "Auto hide time: {}".format(time.time() - start)