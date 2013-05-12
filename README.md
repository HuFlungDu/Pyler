# Pyler

Tiling window manager for windows, written in Python.

Inspired by [xmonad](http://xmonad.org/) and borrowing windows api code from [python windows tiler](https://github.com/Tzbob/python-windows-tiler/blob/master/singleinstance.py). I found out that you could manipulate windows of other applications and this was the first thing that sprang to my mind.

## Config

Configuration is held in a regular Python file,and, since this is written in Python, you can put whatever code you like in there and override any functionality of the code you like. This is a novel idea that I first saw in xmonad and ipython, and I really wish it would be more prevelant. Generally, however, you should call `pyler.config.init` with the following parameters:

    * hotkeys: A dictionary of hotkeys to bind. The key is a hotkey description, the value is a function to bind to

    * float_classes: A list of class names to float initially. Useful for programs that use multiple windows, like the gimp. Currently does nothing.

    * decorate_classes: A list of class names to keep decorated. Useful for windows that won't work without decorations, like chrome.

    * ignore_classes: A list of classes to not add to the tile manager. The normal reason for these is that it couldn't get permission to these anyways. They will stay on top and not go away when you switch desktops.

    * default_tiler: The tiler that each workspace starts on.

    * tilers: A list of tilers to use.

The Python module must contain a function `init`, which takes no arguments and has no necessary return value. This function should initialize the config for use, usually calling `pyler.config.init`. Pyler comes with a default config, to override that config, run pyler with the -c option, e.g. `python main.py -c myconfig.py`.

## Hotkeys

Hotkeys are described as a tuple, the first element in a mask, using bitwise or to select mutliple mods, e.g. `mod_super|mod_shift` would match holding the windows button and the shift button when you press the key. The second element of the tuple is the key pressed, e.g. `k_j` would match `j`, `k_Return` matches the enter key, etcetera. The keys are defined in `pyler.keycodes`. The value for the dictionary is a function to be called. The function must take at least one value, which is the key that was pressed. A finished hotkey description might look like this: `(mod_super|mod_shift,k_Return)`.

## Tilers

Tilers can be defined by the user and sent to the config from a users config file. A tiler is described simply as an object that has a `name` property that is a string and a `tile` function that takes the following parameters:

    * dimmensions: An object with an x, y, width, and height properties, representing the dimmensions of the monitor the workspace occupies.

    * main_windows: The number of windows in the main area of the workspace.

    * main_area_size: The size of the main area, expressed as a float between 0 and 1.

    * active_window: The current active window.

    * windows: A list of windows to be tiled.

The preferred effect of this function is to have it tile the windows accordingly, but there is no check to make sure that actually happens.

The internal tilers (`tall`,`mirrortall`, and `full`) are implemented as modules (accessible through `pyler.tilers.(tall|mirrortall|full)`), but there is nothing stopping you from implementing them as classes, static classes, named tuples, empty classes, functions with added properties, basically anything that can be accessed by `tiler.tile(*args)` will do just fine.

## Install

Currently, there is no install process, there is no installer, and there is no real packaging system. Just clone the repo and run main.py, probably on boot. The prerequisites are:

   * [Python 2.7](http://www.python.org/getit/)
   * [pywin32](http://sourceforge.net/projects/pywin32/)

