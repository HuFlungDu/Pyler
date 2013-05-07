
class WindowNotFoundError(Exception):
    pass

class Tiler(object):
    def add_window(self, window):
        pass
    def remove_windw(self,window):
        pass
    def move_window_up(self, window):
        pass
    def move_window_down(self,window):
        pass
    def switch_window_up(self):
        pass
    def swtich_window_down(self):
        pass
    def set_active_window(self):
        pass
    def increase_main_area_size(self):
        pass
    def decrease_main_area_size(self):
        pass
    def increase_main_area_window_count(self):
        pass
    def decrease_main_area_window_count(self):
        pass

class TallTiler(Tiler):
    name = "Tall"
    def __init__(self, monitor):
        self._monitor = monitor
        self._windows = []
        self._main_windows = 1
        self._main_width = monitor.width//2
        self._active_window = 0
        self._hidden = False

    def hide(self):
        for window in self._windows:
            window.hide()
        self._hidden = True

    def show(self):
        for window in self._windows:
            window.show()
        self._hidden = False
        self._retile()

    def add_window(self, window):
        if window not in self._windows:
            self._windows.append(window)
            self._active_window = len(self._windows)-1
            self._retile()

    def remove_window(self,window):
        try:
            self._windows.remove(window)
            self._retile()
        except ValueError:
            raise WindowNotFoundError("Given window not found in tiler")

    def move_window_up(self, window):
        try:
            index = self._windows.index(window)
            if index > 0:
                self._windows[index-1],self._windows[index] = self._windows[index],self._windows[index-1]
                self._retile()
        except ValueError:
            raise WindowNotFoundError("Given window not found in tiler")
        
    def move_window_down(self,window):
        try:
            index = self._windows.index(window)
            if index < len(self._windows)-1:
                self._windows[index+1],self._windows[index] = self._windows[index],self._windows[index+1]
                self._retile()
        except ValueError:
            raise WindowNotFoundError("Given window not found in tiler")
        
    def switch_window_up(self):
        self._active_window = (self._active_window - 1) % len(self._windows)

    def swtich_window_down(self):
        self._active_window = (self._active_window + 1) % len(self._windows)

    def set_active_window(self, window):
        try:
            self._active_window = self._windows.index(window)
        except ValueError:
            raise WindowNotFoundError("Given window not found in tiler")
        pass
    def increase_main_area_size(self):
        pass
    def decrease_main_area_size(self):
        pass
    def increase_main_area_window_count(self):
        self._main_windows += 1
        self._retile()
        pass
    def decrease_main_area_window_count(self):
        self._main_windows = max(self._main_windows-1,0)
        self._retile()
        pass

    def _retile(self):
        if not self._hidden:
            for i, window in enumerate(self._windows):
                if i < self._main_windows:
                    try:
                        height = self._monitor.height/min(self._main_windows,len(self._windows))
                    except ZeroDivisionError:
                        print "This should never happen"
                    width = self._monitor.width if len(self._windows) < self._main_windows else self._main_width
                    x = self._monitor.x
                    y = self._monitor.y + height*i
                else:
                    height = self._monitor.height/(len(self._windows)-self._main_windows)
                    width = self._monitor.width - self._main_width
                    x = self._monitor.x + self._main_width
                    y = self._monitor.y + height*(i-self._main_windows)
                window.set_position(x,y,width,height)

