import pyler
from pyler.exceptions import *
from pyler import monitor

import win32gui
import win32con

def quit():
    raise EndProgram

def switch_workspace(workspace):
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

def send_to_workspace(workspace):
    newworkspace = pyler.workspaces[workspace]
    workspace = pyler.active_monitor.get_workspace()
    if workspace != newworkspace:
        active = workspace.get_active_window()
        workspace.remove_window(active)
        newworkspace.add_window(active)

def increase_main_area_window_count():
    pyler.active_monitor.get_workspace().increase_main_area_window_count()

def decrease_main_area_window_count():
    pyler.active_monitor.get_workspace().decrease_main_area_window_count()

def destroy_active_window():
    if win32gui.GetForegroundWindow() != 0:
        win32gui.SendMessage(win32gui.GetForegroundWindow(), win32con.WM_CLOSE, 0, 0)

def switch_window_up():
    pyler.active_monitor.get_workspace().switch_window_up()

def switch_window_down():
    pyler.active_monitor.get_workspace().switch_window_down()

def move_window_up():
    pyler.active_monitor.get_workspace().move_window_up()

def move_window_down():
    pyler.active_monitor.get_workspace().move_window_down()

def cycle_tilers(tilers):
    newtiler = tilers[(tilers.index(pyler.active_monitor.get_workspace().tiler)+1)%len(tilers)]
    pyler.active_monitor.get_workspace().set_tiler(newtiler)

def toggle_struts():
    workspace = pyler.active_monitor.get_workspace()
    workspace.toggle_struts()

def add_to_tiled():
    workspace = pyler.active_monitor.get_workspace()
    active = workspace.get_active_window()
    workspace.unfloat_window(active)