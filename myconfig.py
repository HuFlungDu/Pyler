from pyler import config
from pyler import actions
from pyler.keycodes import *
from pyler.tilers import *

import subprocess

default_tiler = tall
tilers = [tall,mirrortall,full]

hotkeys = {
    (mod_super,k_1): (actions.switch_workspace,1),
    (mod_super,k_2): (actions.switch_workspace,2),
    (mod_super,k_3): (actions.switch_workspace,3),
    (mod_super,k_4): (actions.switch_workspace,4),
    (mod_super,k_5): (actions.switch_workspace,5),
    (mod_super,k_6): (actions.switch_workspace,6),
    (mod_super,k_7): (actions.switch_workspace,7),
    (mod_super,k_8): (actions.switch_workspace,8),
    (mod_super,k_9): (actions.switch_workspace,9),
    (mod_super|mod_shift,k_1): (actions.send_to_workspace,1),
    (mod_super|mod_shift,k_2): (actions.send_to_workspace,2),
    (mod_super|mod_shift,k_3): (actions.send_to_workspace,3),
    (mod_super|mod_shift,k_4): (actions.send_to_workspace,4),
    (mod_super|mod_shift,k_5): (actions.send_to_workspace,5),
    (mod_super|mod_shift,k_6): (actions.send_to_workspace,6),
    (mod_super|mod_shift,k_7): (actions.send_to_workspace,7),
    (mod_super|mod_shift,k_8): (actions.send_to_workspace,8),
    (mod_super|mod_shift,k_9): (actions.send_to_workspace,9),
    (mod_super,k_Comma): actions.increase_main_area_window_count,
    (mod_super,k_Period): actions.decrease_main_area_window_count,
    (mod_super|mod_shift,k_Return): lambda: subprocess.call("start cmd", shell=True),
    (mod_super,k_t): actions.add_to_tiled,
    (mod_super,k_b): actions.toggle_struts,
    (mod_super|mod_shift,k_b): lambda: subprocess.call("start chrome", shell=True),
    (mod_super|mod_shift,k_f): lambda: subprocess.call("start explorer", shell=True),
    (mod_super|mod_shift,k_c): actions.destroy_active_window,
    (mod_super,k_j): actions.switch_window_up,
    (mod_super,k_k): actions.switch_window_down,
    #(mod_super,k_Up):switch_window_up,
    #(mod_super,k_Down):switch_window_down,
    (mod_super|mod_shift,k_j): actions.move_window_up,
    (mod_super|mod_shift,k_k): actions.move_window_down,
    #(mod_super|mod_shift,k_Up):move_window_up,
    #(mod_super|mod_shift,k_Down):move_window_down,
    (mod_super,k_Space): (actions.cycle_tilers,tilers),
    (mod_super|mod_shift,k_q): actions.quit
}

float_classes = []
decorate_classes = ["Chrome_WidgetWin_0","Chrome_WidgetWin_1"]
ignore_classes = []

def init():
    config.init(hotkeys=hotkeys,
                float_classes=float_classes,
                decorate_classes=decorate_classes,
                ignore_classes=ignore_classes,
                default_tiler=default_tiler,
                tilers=tilers)

