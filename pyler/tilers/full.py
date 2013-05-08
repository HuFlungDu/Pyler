name = "Full"

def tile(dimmensions, main_windows, main_area_size, active_window, windows):
    if len(windows):
        for window in windows:
            window.set_position(*dimmensions)
        active_window.set_position(*dimmensions)

