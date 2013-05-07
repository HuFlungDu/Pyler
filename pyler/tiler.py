name = "Tall"

def tile(self, dimmensions, main_windows, main_area_size, windows):
    dimmensions = self._workspace.get_monitor_dimmensions()
    for i, window in enumerate(self._windows):
        if i < self._main_windows:
            try:
                height = dimmensions.height/min(self._main_windows,len(self._windows))
            except ZeroDivisionError:
                print "This should never happen"
            width = dimmensions.width if len(self._windows) <= self._main_windows else self._main_width*dimmensions.width
            x = dimmensions.x
            y = dimmensions.y + height*i
        else:
            height = dimmensions.height/(len(self._windows)-self._main_windows)
            width = dimmensions.width - self._main_width*dimmensions.width if self._main_windows > 0 else dimmensions.width
            x = dimmensions.x + self._main_width*dimmensions.width if self._main_windows > 0 else dimmensions.x
            y = dimmensions.y + height*(i-self._main_windows)
        window.set_position(x,y,width,height)

