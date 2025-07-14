from evdev import UInput
from evdev import ecodes as e

from linux_hotkey.classes import Key, KeyEventAction, Shortcut


def ctrl_p_action(virtual_device: UInput) -> bool:
    virtual_device.write(e.EV_KEY, e.KEY_A, KeyEventAction.DOWN)
    virtual_device.write(e.EV_KEY, e.KEY_A, KeyEventAction.UP)
    virtual_device.syn()
    return True


SHORTCUTS = [Shortcut(Key(e.KEY_P), ctrl_p_action, (Key(e.KEY_LEFTCTRL),))]
