import ctypes
import win32gui
import win32api
import win32con

import pyler
from pyler import keycodes
from pyler import monitor
from pyler import config
from pyler import workspace
from pyler import window
from pyler import hotkey

import sys
import traceback


def main():
    if not ctypes.windll.user32.RegisterShellHookWindow(pyler.pseudo_window):
        print win32api.FormatMessage(win32api.GetLastError())
        return

    try:
        while True:
            message = win32gui.GetMessage(pyler.pseudo_window,0,0)
            if message[1][1] == win32con.WM_HOTKEY:
                try:
                    hotkey.execute(message[1][2])
                except config.EndProgram:
                    break
            elif message[1][2] == win32con.HSHELL_WINDOWCREATED:
                if message[1][3] != 0 and window.is_valid(message[1][3]):
                    newwindow = window.Window(message[1][3])
                    if newwindow not in pyler.get_all_windows():
                        pyler.active_monitor.get_workspace().add_window(newwindow)
                
            elif message[1][2] == win32con.HSHELL_WINDOWDESTROYED:
                try:
                    pyler.active_monitor.get_workspace().remove_window(window.Window(message[1][3]))
                except:
                    pass

            elif message[1][2] == win32con.HSHELL_WINDOWACTIVATED:
                try:
                    pyler.active_monitor.get_workspace().get_tiler().set_active_window(window.Window(message[1][3]))
                except:
                    pass
    except:
        print sys.exc_info()[0]
        traceback.print_exc()
    finally:
        for ws in pyler.workspaces:
            for w in pyler.workspaces[ws]._windows:
                try:
                    w.show()
                except:
                    pass

if __name__ == '__main__':
    main()