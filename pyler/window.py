import win32gui
import win32api
import win32con

def is_valid(window):
    if win32gui.IsWindowVisible(window):
        if not win32gui.GetParent(window):
            value = win32gui.GetWindowLong(window, win32con.GWL_EXSTYLE)
            owner = win32gui.GetWindow(window, win32con.GW_OWNER)
            if (not owner and not value & win32con.WS_EX_TOOLWINDOW) or value & win32con.WS_EX_APPWINDOW:
                return True
    return False

def get_valid_windows():
    windows = []
    def enum_callback(window, ph):
        if is_valid(window):
            windows.append(Window(window))
    win32gui.EnumWindows(enum_callback, None)
    return windows



def window_under_cursor():
    return Window(win32gui.WindowFromPoint(win32api.GetCursorPos()))

def find_window(name):
    return Window(win32gui.FindWindow(name, None))


class Window(object):
    def __init__(self,window):
        assert window != 0
        self._window = window
        self.floating = False

    def __eq__(self, other):
        return self._window == other.get_window()

    def __hash__(self):
        return hash(self._window)

    def get_window(self):
        return self._window

    def set_position(self,x,y,width,height):
        try:
            win32gui.MoveWindow(self._window,int(x),int(y),int(width),int(height),True)
        except Exception as e:
            print self.get_class_name()
            raise e

    def show(self):
        win32gui.ShowWindow(self._window, win32con.SW_SHOWNORMAL)

    def hide(self):
        win32gui.ShowWindow(self._window, win32con.SW_HIDE)

    def focus(self):
        try:
            win32gui.SetForegroundWindow(self._window)
        except:
            pass
        #win32gui.SetFocus(self._window)

    def bring_to_foreground(self):
        win32gui.SetForegroundWindow(self._window)

    def is_decorated(self):
        return bool(win32gui.GetWindowLong(self._window, win32con.GWL_STYLE) & win32con.WS_CAPTION)

    def get_class_name(self):
        return win32gui.GetClassName(self._window)

    def undecorate(self):
        if self.is_decorated():
            style = win32gui.GetWindowLong(self._window, win32con.GWL_STYLE)
            style -= win32con.WS_CAPTION 
            win32gui.SetWindowLong(self._window, win32con.GWL_STYLE, style)

    def decorate(self):
        if not self.is_decorated():
            style = win32gui.GetWindowLong(self._window, win32con.GWL_STYLE)
            style += win32con.WS_CAPTION
            win32gui.SetWindowLong(self._window, win32con.GWL_STYLE, style)

    def toggle_decoration(self):
        if is_valid(self._window):
            if self.is_decorated():
                self.undecorate()
            else:
                self.decorate()
            self.update()

    def update(self):
        win32gui.SetWindowPos(self._window
                    ,0
                    ,0
                    ,0
                    ,0
                    ,0
                    ,win32con.SWP_FRAMECHANGED + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE + win32con.SWP_NOZORDER
            )

    def exists(self):
        return win32gui.IsWindow(self._window)

    @property
    def classname(self):
        return win32gui.GetClassName(self._window)