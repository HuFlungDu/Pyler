import win32api

def get_monitors():
    monitors = []
    for monitor in win32api.EnumDisplayMonitors():
        monitors.append(Monitor(monitor[0]))
    return monitors

class Monitor(object):
    def __init__(self,monitor):
        self._monitor = monitor
        self._workspace = None

    def get_workspace(self):
        return self._workspace

    def set_workspace(self, workspace):
        self._workspace = workspace
        self._workspace.set_monitor(self)

    @property
    def dimmensions(self):
        return win32api.GetMonitorInfo(self._monitor)["Work"]

    @property
    def width(self):
        return self.dimmensions[2] - self.x

    @property
    def height(self):
        return self.dimmensions[3] - self.y

    @property
    def x(self):
        return self.dimmensions[0]

    @property
    def y(self):
        return self.dimmensions[1]