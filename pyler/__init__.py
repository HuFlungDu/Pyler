import hotkey
import monitor
import workspace
import window
import config
import win32gui
import win32con
import collections
import taskbar


global pseudo_window
global monitors
global active_monitor
global statusbar
global workspaces
def init():
    global pseudo_window
    global monitors
    global active_monitor
    global statusbar
    global workspaces
    _window_class_name = "pseudo"
    _window_class = win32gui.WNDCLASS()
    _instance = _window_class.hInstance = win32gui.GetModuleHandle(None)
    _window_class.lpszClassName = _window_class_name
    _window_class.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW;
    _window_class.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
    _window_class.hbrBackground = win32con.COLOR_WINDOW
    _classAtom = win32gui.RegisterClass(_window_class)

    # Create the Window.
    _style = win32con.WS_OVERLAPPED
    pseudo_window = win32gui.CreateWindow(_classAtom,
            _window_class_name,
            _style,
            0,
            0,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            0,
            0,
            _instance,
            None)
    win32gui.ShowWindow(pseudo_window,0)
    win32gui.UpdateWindow(pseudo_window)


    monitors = monitor.get_monitors()
    active_monitor = monitors[0]
    # I'd like to make this more generic
    statusbar = taskbar.Taskbar()

    config.init()

    workspaces = collections.OrderedDict()
    for i in xrange(1,10):
        workspaces[i] = workspace.Workspace(i,config.default_tiler)
    for w, i in zip(workspaces,xrange(len(monitors))):
        monitors[i].set_workspace(workspaces[w])

    for key_combo in config.hotkeys:
        hotkey.register_hotkey(key_combo[1],key_combo[0],config.hotkeys[key_combo])
    windows = window.get_valid_windows()[::-1]
    workspaceiter = iter(workspaces)
    w = workspaceiter.next()
    for vwindow in windows:
        if vwindow.get_class_name() not in config.ignore_classes:
            workspaces[w].add_window(vwindow)
    for w in workspaceiter:
        workspaces[w].hide()

def get_all_windows():
    windows = []
    for ws in workspaces:
        windows.extend(workspaces[ws].get_windows())
    return windows