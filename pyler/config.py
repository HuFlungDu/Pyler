import pyler
from pyler.tilers import tall,mirrortall,full
from pyler import keycodes
from pyler.keycodes import *

import subprocess
import win32gui
import win32con

default_tiler = tall
tilers = [tall,mirrortall,full]

class EndProgram(Exception):
    pass

def quit(hotkey):
    raise EndProgram

def switch_workspace(hotkey,workspace):
    monitor = None
    for monitor in [x for x in pyler.monitors if x != pyler.active_monitor]:
        if monitor.get_workspace == pyler.workspaces[workspace]:
            break
    newworkspace = pyler.workspaces[workspace]
    workspace = pyler.active_monitor.get_workspace()
    if newworkspace != workspace:
        if monitor is not None:
            monitor.set_workspace(workspace)
        else:
            workspace.set_monitor(None)
        pyler.active_monitor.set_workspace(newworkspace)

def send_to_workspace(hotkey,workspace):
    newworkspace = pyler.workspaces[workspace]
    workspace = pyler.active_monitor.get_workspace()
    if workspace != newworkspace:
        active = workspace.get_active_window()
        workspace.remove_window(active)
        newworkspace.add_window(active)

def increase_main_area_window_count(hotkey):
    pyler.active_monitor.get_workspace().increase_main_area_window_count()

def decrease_main_area_window_count(hotkey):
    pyler.active_monitor.get_workspace().decrease_main_area_window_count()

def destroy_active_window(hotkey):
    if win32gui.GetForegroundWindow() != 0:
        win32gui.SendMessage(win32gui.GetForegroundWindow(), win32con.WM_CLOSE, 0, 0)

def switch_window_up(hotkey):
    pyler.active_monitor.get_workspace().switch_window_up()

def switch_window_down(hotkey):
    pyler.active_monitor.get_workspace().switch_window_down()

def move_window_up(hotkey):
    pyler.active_monitor.get_workspace().move_window_up()

def move_window_down(hotkey):
    pyler.active_monitor.get_workspace().move_window_down()

def cycle_tilers(hotkey):
    newtiler = tilers[(tilers.index(pyler.active_monitor.get_workspace().tiler)+1)%len(tilers)]
    pyler.active_monitor.get_workspace().set_tiler(newtiler)

def toggle_struts(hotkey):
    workspace = pyler.active_monitor.get_workspace()
    workspace.toggle_struts()

global hotkeys
global float_classes
global decorate_classes
global ignore_classes

hotkeys = {
    (mod_super,k_1): lambda x: switch_workspace(x,1),
    (mod_super,k_2): lambda x: switch_workspace(x,2),
    (mod_super,k_3): lambda x: switch_workspace(x,3),
    (mod_super,k_4): lambda x: switch_workspace(x,4),
    (mod_super,k_5): lambda x: switch_workspace(x,5),
    (mod_super,k_6): lambda x: switch_workspace(x,6),
    (mod_super,k_7): lambda x: switch_workspace(x,7),
    (mod_super,k_8): lambda x: switch_workspace(x,8),
    (mod_super,k_9): lambda x: switch_workspace(x,9),
    (mod_super|mod_shift,k_1): lambda x: send_to_workspace(x,1),
    (mod_super|mod_shift,k_2): lambda x: send_to_workspace(x,2),
    (mod_super|mod_shift,k_3): lambda x: send_to_workspace(x,3),
    (mod_super|mod_shift,k_4): lambda x: send_to_workspace(x,4),
    (mod_super|mod_shift,k_5): lambda x: send_to_workspace(x,5),
    (mod_super|mod_shift,k_6): lambda x: send_to_workspace(x,6),
    (mod_super|mod_shift,k_7): lambda x: send_to_workspace(x,7),
    (mod_super|mod_shift,k_8): lambda x: send_to_workspace(x,8),
    (mod_super|mod_shift,k_9): lambda x: send_to_workspace(x,9),
    (mod_super,k_Comma): increase_main_area_window_count,
    (mod_super,k_Period): decrease_main_area_window_count,
    (mod_super|mod_shift,k_Return): lambda x: subprocess.call("start cmd", shell=True),
    (mod_super,k_b): toggle_struts,
    (mod_super|mod_shift,k_b): lambda x: subprocess.call("start chrome", shell=True),
    (mod_super|mod_shift,k_c): destroy_active_window,
    (mod_super,k_j):switch_window_up,
    (mod_super,k_k):switch_window_down,
    #(mod_super,k_Up):switch_window_up,
    #(mod_super,k_Down):switch_window_down,
    (mod_super|mod_shift,k_j):move_window_up,
    (mod_super|mod_shift,k_k):move_window_down,
    #(mod_super|mod_shift,k_Up):move_window_up,
    #(mod_super|mod_shift,k_Down):move_window_down,
    (mod_super,k_Space):cycle_tilers,
    (mod_super|mod_shift,k_q): quit
}

float_classes = []
decorate_classes = ["Chrome_WidgetWin_0","Chrome_WidgetWin_1"]
ignore_classes = []

def init(hk=hotkeys,fc=float_classes,dc=decorate_classes,ic=ignore_classes):
    global hotkeys
    global float_classes
    global decorate_classes
    global ignore_classes
    hotkeys = hk
    float_classes = fc
    decorate_classes = dc
    ignore_classes = ic