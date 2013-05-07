name = "Full"

def tile(dimmensions, main_windows, main_area_size, active_window, windows):
    for i, window in enumerate(windows):
        window.set_position(*dimmensions)
    active_window.set_position(*dimmensions)

