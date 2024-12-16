from time import sleep

import keyboard



import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

scr = Wnck.Screen.get_default()
scr.force_update()
windows = scr.get_windows()
names = [w.get_name() for w in windows]
screen = Wnck.Screen
print(scr.get_active_window().get_name())

while True:
    scr.force_update()
    windows = scr.get_windows()
    names = [w.get_name() for w in windows]
    active = scr.get_active_window().get_name()
    for i, w in enumerate(scr.get_windows()):
        print(f"{i}: {w.get_name()}")
    sleep(3)

