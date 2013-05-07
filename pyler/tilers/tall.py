name = "Tall"

def tile(dimmensions, main_windows, main_area_size, windows):
    for i, window in enumerate(windows):
        if i < main_windows:
            try:
                height = dimmensions.height/min(main_windows,len(windows))
            except ZeroDivisionError:
                print "This should never happen"
                raise Exception
            width = dimmensions.width if len(windows) <= main_windows else main_area_size*dimmensions.width
            x = dimmensions.x
            y = dimmensions.y + height*i
        else:
            height = dimmensions.height/(len(windows)-main_windows)
            width = dimmensions.width - main_area_size*dimmensions.width if main_windows > 0 else dimmensions.width
            x = dimmensions.x + main_area_size*dimmensions.width if main_windows > 0 else dimmensions.x
            y = dimmensions.y + height*(i-main_windows)
        window.set_position(x,y,width,height)

