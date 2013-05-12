import pyler
from pyler.tilers import tall,mirrortall,full
from pyler import actions
from pyler.keycodes import *

import subprocess
import win32gui
import win32con



global hotkeys
global float_classes
global decorate_classes
global ignore_classes
global default_tiler
global tilers


default_tiler = tall
tilers = [tall,mirrortall,full]

hotkeys = {
    (mod_super,k_1): lambda x: actions.switch_workspace(x,1),
    (mod_super,k_2): lambda x: actions.switch_workspace(x,2),
    (mod_super,k_3): lambda x: actions.switch_workspace(x,3),
    (mod_super,k_4): lambda x: actions.switch_workspace(x,4),
    (mod_super,k_5): lambda x: actions.switch_workspace(x,5),
    (mod_super,k_6): lambda x: actions.switch_workspace(x,6),
    (mod_super,k_7): lambda x: actions.switch_workspace(x,7),
    (mod_super,k_8): lambda x: actions.switch_workspace(x,8),
    (mod_super,k_9): lambda x: actions.switch_workspace(x,9),
    (mod_super|mod_shift,k_1): lambda x: actions.send_to_workspace(x,1),
    (mod_super|mod_shift,k_2): lambda x: actions.send_to_workspace(x,2),
    (mod_super|mod_shift,k_3): lambda x: actions.send_to_workspace(x,3),
    (mod_super|mod_shift,k_4): lambda x: actions.send_to_workspace(x,4),
    (mod_super|mod_shift,k_5): lambda x: actions.send_to_workspace(x,5),
    (mod_super|mod_shift,k_6): lambda x: actions.send_to_workspace(x,6),
    (mod_super|mod_shift,k_7): lambda x: actions.send_to_workspace(x,7),
    (mod_super|mod_shift,k_8): lambda x: actions.send_to_workspace(x,8),
    (mod_super|mod_shift,k_9): lambda x: actions.send_to_workspace(x,9),
    (mod_super,k_Comma): actions.increase_main_area_window_count,
    (mod_super,k_Period): actions.decrease_main_area_window_count,
    (mod_super|mod_shift,k_Return): lambda x: subprocess.call("start cmd", shell=True),
    (mod_super,k_b): actions.toggle_struts,
    (mod_super|mod_shift,k_b): lambda x: subprocess.call("start chrome", shell=True),
    (mod_super|mod_shift,k_c): actions.destroy_active_window,
    (mod_super,k_j): actions.switch_window_up,
    (mod_super,k_k): actions.switch_window_down,
    #(mod_super,k_Up):switch_window_up,
    #(mod_super,k_Down):switch_window_down,
    (mod_super|mod_shift,k_j): actions.move_window_up,
    (mod_super|mod_shift,k_k): actions.move_window_down,
    #(mod_super|mod_shift,k_Up):move_window_up,
    #(mod_super|mod_shift,k_Down):move_window_down,
    (mod_super,k_Space): lambda x: actions.cycle_tilers(x,tilers),
    (mod_super|mod_shift,k_q): actions.quit
}

float_classes = []
decorate_classes = ["Chrome_WidgetWin_0","Chrome_WidgetWin_1"]
ignore_classes = []

def init(hotkeys=hotkeys,
         float_classes=float_classes,
         decorate_classes=decorate_classes,
         ignore_classes=ignore_classes,
         default_tiler=default_tiler,
         tilers=tilers):
    globs = globals()
    globs["hotkeys"] = hotkeys
    globs["float_classes"] = float_classes
    globs["decorate_classes"] = decorate_classes
    globs["ignore_classes"] = ignore_classes
    globs["default_tiler"] = default_tiler
    globs["tilers"] = tilers