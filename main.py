import ctypes
import win32gui
import win32api
import win32con

import singleinstance
try:
    mutex = singleinstance.get_mutex()
except singleinstance.ApplicationAlreadyrunning:
    print "Application already running"
    exit()

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
    pyler.init()
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
                    #print message[1][3]
                    newwindow = window.Window(message[1][3])
                    if newwindow not in pyler.get_all_windows():
                        pyler.active_monitor.get_workspace().add_window(newwindow)
                
            elif message[1][2] == win32con.HSHELL_WINDOWDESTROYED:
                try:
                    win = window.Window(message[1][3])
                    ws = pyler.active_monitor.get_workspace()
                    ws.remove_window(win)
                    if not win.exists():
                        [w.remove_window(win) for w in pyler.workspaces.values() if w != ws]
                    #pyler.active_monitor.get_workspace().remove_window(window.Window(message[1][3]))

                except Exception as e:
                    #print e
                    pass

            elif message[1][2] == win32con.HSHELL_WINDOWACTIVATED:
                try:
                    if message[1][3] > 0:
                        win = window.Window(message[1][3])
                        if win.get_class_name() not in config.ignore_classes:
                            pyler.active_monitor.get_workspace().set_active_window(win)
                except Exception as e:
                    pass
    except:
        #pass
        print sys.exc_info()[0]
        traceback.print_exc()
    finally:
        pyler.statusbar.show()
        for w in pyler.get_all_windows():
            try:
                w.show()
                w.decorate()
            except Exception as e:
                print e
                pass

if __name__ == '__main__':
    main()
    singleinstance.close(mutex)