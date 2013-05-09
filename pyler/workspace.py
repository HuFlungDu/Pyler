import collections
import pyler
from pyler import config

class WindowNotFoundError(Exception):
    pass

class Workspace(object):
    def __init__(self,number, tiler):
        self.number = number
        self._monitor = None
        self.tiler = tiler
        self._windows = []
        self._tiled_windows = []
        self._floating_windows = []
        self._main_windows = 1
        self._main_size = .5
        self._active_window = None
        self._hidden = False
        self._show_taskbar = True

    def add_window(self,window):
        if window not in self._windows:
            self._windows.append(window)
            if not self._hidden:
                window.show()
                if window.get_class_name() not in config.decorate_classes:
                    window.undecorate()
            if not window.floating:
                try:
                    self._tiled_windows.insert(self._tiled_windows.index(self._active_window), window)
                except ValueError:
                    self._tiled_windows.append(window)
            else:
                self._floating_windows.append(window)
            self._active_window = window
            self._retile()

    def remove_window(self,window):
        if window in self._windows:
            self._windows.remove(window)
            if window.floating:
                self._floating_windows.remove(window)
            else:
                index = self._tiled_windows.index(self._active_window)
                self._tiled_windows.remove(window)
                if len(self._tiled_windows):
                    self._active_window = self._tiled_windows[index % len(self._tiled_windows)]
                elif len(self._floating_windows):
                    self._active_window = self._floating_windows[-1]
                else:
                    self._active_window = None
            try:
                window.hide()
            except:
                pass
            self._retile()

    def toggle_struts(self):
        if self._show_taskbar:
            pyler.statusbar.hide()
            self._show_taskbar = False
        else:
            pyler.statusbar.show()
            self._show_taskbar = True
        self._retile()

    def hide(self):
        for window in self._windows:
            window.hide()
        self._hidden = True
        #self.tiler.hide()

    def show(self):
        for window in self._tiled_windows:
            window.show()
        for window in self._floating_windows:
            window.show()
        if self._active_window is not None:
            self._active_window.focus()
        if self._show_taskbar:
            pyler.statusbar.show()
        else:
            pyler.statusbar.hide()
        self._hidden = False
        self._retile()
        #self.tiler.show()

    def get_windows(self):
        return self._windows

    def get_monitor(self):
        return self._monitor

    def set_monitor(self,monitor):
        self._monitor = monitor
        if monitor is None:
            self.hide()
        else:
            self.show()

    def set_tiler(self, tiler):
        self.tiler = tiler
        self._retile()

    def get_monitor_dimmensions(self):
        Dimmensions = collections.namedtuple('Dimmensions', ['x', 'y',"width","height"])
        if self._monitor is not None:
            return Dimmensions(self._monitor.x,self._monitor.y,self._monitor.width,self._monitor.height)
        else:
            return Dimmensions(0,0,0,0)

    def move_window_up(self):
        try:
            if self._active_window in self._tiled_windows:
                index = self._tiled_windows.index(self._active_window)
                newindex = (index-1) % len(self._tiled_windows)
                self._tiled_windows[newindex],self._tiled_windows[index] = self._tiled_windows[index],self._tiled_windows[newindex]
                self._retile()
            else:
                index = self._floating_windows.index(self._active_window)
                newindex = (index+1) % len(self._floating_windows)
                self._floating_windows[newindex],self._floating_windows[index] = self._floating_windows[index],self._floating_windows[newindex]
                self._retile()
        except ValueError:
            raise WindowNotFoundError("Given window not found in tiler")
        
    def move_window_down(self):
        try:
            if self._active_window in self._tiled_windows:
                index = self._tiled_windows.index(self._active_window)
                newindex = (index+1) % len(self._tiled_windows)
                self._tiled_windows[newindex],self._tiled_windows[index] = self._tiled_windows[index],self._tiled_windows[newindex]
                self._retile()
            else:
                index = self._floating_windows.index(self._active_window)
                newindex = (index-1) % len(self._floating_windows)
                self._floating_windows[newindex],self._floating_windows[index] = self._floating_windows[index],self._floating_windows[newindex]
                self._retile()
        except ValueError:
            raise WindowNotFoundError("Given window not found in tiler")
        
    def switch_window_up(self):
        windows = self._tiled_windows + self._floating_windows
        self._active_window = windows[(windows.index(self._active_window) - 1) % len(windows)]
        self._active_window.focus()

    def switch_window_down(self):
        windows = self._tiled_windows + self._floating_windows
        self._active_window = windows[(windows.index(self._active_window) + 1) % len(windows)]
        self._active_window.focus()

    def get_active_window(self):
        return self._active_window

    def set_active_window(self, window):
        if window in self._windows:
            self._active_window = window
            window.focus()
        else:
            raise WindowNotFoundError("Given window not found in tiler")

    def increase_main_area_size(self):
        pass
    def decrease_main_area_size(self):
        pass
    def increase_main_area_window_count(self):
        self._main_windows += 1
        self._retile()

    def decrease_main_area_window_count(self):
        self._main_windows = max(self._main_windows-1,0)
        self._retile()

    def _retile(self):
        if not self._hidden:
            self.tiler.tile(self.get_monitor_dimmensions(), self._main_windows, self._main_size, self._active_window, self._tiled_windows)