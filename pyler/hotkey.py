import ctypes
import win32con
import win32api

import pyler
from pyler import keycodes

hotkeys = {}

class HotkeyRegistrationFailure(Exception):
    pass
class HotkeyUnRegistrationFailure(Exception):
    pass
class HotkeyExecutionFailure(Exception):
    pass

class HotKey(object):
    def __init__(self,key,modifiers,key_id):
        self.key = key
        self.modifiers = modifiers
        self.key_id = key_id

def register_hotkey(key,modifiers,callback,*userdata):
    i = 1
    while i in hotkeys:
        i += 1
    if ctypes.windll.user32.RegisterHotKey(pyler.pseudo_window, i, modifiers, key):
        hotkeys[i] = (callback,HotKey(key,modifiers,i))+userdata
        return i
    else:
        raise HotkeyRegistrationFailure(win32api.FormatMessage(win32api.GetLastError()))
    

def unregister_hotkey(hotkey_id):
    try:
        assert hotkey_id in hotkeys
        assert ctypes.windll.user32.UnRegisterHotKey(pyler.pseudo_window,hotkey_id)
    except AssertionError:
        raise HotkeyUnRegistrationFailure


def execute(hotkey_id):
    try:
        function, hotkey, userdata = hotkeys[hotkey_id][0], hotkeys[hotkey_id][1], hotkeys[hotkey_id][2:]
        function(*userdata)
    except KeyError:
        raise HotkeyExecutionFailure