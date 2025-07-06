from evdev import InputDevice
from evdev import ecodes as e

from linux_hotkey.classes import InputType, Key
from linux_hotkey.input_device_utils import get_input_device

MODIFIER_KEYS = {
    Key(e.KEY_LEFTCTRL): False,
    Key(e.KEY_LEFTSHIFT): False,
    Key(e.KEY_LEFTALT): False,
    Key(e.KEY_RIGHTCTRL): False,
    Key(e.KEY_RIGHTSHIFT): False,
    Key(e.KEY_RIGHTALT): False,
}

STATE_KEYS = {
    Key(e.KEY_NUMLOCK): False,
    Key(e.KEY_CAPSLOCK): False,
}


MOUSE_INPUT = get_input_device(InputType.MOUSE)
KEYBOARD_INPUT = get_input_device(InputType.KEYBOARD)

INPUT_DEVICES: dict[InputType, InputDevice] = {
    InputType.MOUSE: MOUSE_INPUT,
    InputType.KEYBOARD: KEYBOARD_INPUT,
}
