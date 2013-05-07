name = "MirrorTall"

def tile(dimmensions, main_windows, main_area_size, active_window, windows):
    for i, window in enumerate(windows):
        if i < main_windows:
            try:
                width = dimmensions.width/min(main_windows,len(windows))
            except ZeroDivisionError:
                print "This should never happen"
                raise Exception
            height = dimmensions.height if len(windows) <= main_windows else main_area_size*dimmensions.height
            x = dimmensions.x + width*i
            y = dimmensions.y
        else:
            width = dimmensions.width/(len(windows)-main_windows)
            height = dimmensions.height - main_area_size*dimmensions.height if main_windows > 0 else dimmensions.height
            y = dimmensions.y + main_area_size*dimmensions.height if main_windows > 0 else dimmensions.y
            x = dimmensions.x + width*(i-main_windows)
        window.set_position(x,y,width,height)

