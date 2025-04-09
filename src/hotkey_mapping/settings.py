import os

import evdev
from evdev import InputDevice
from evdev import ecodes as e

from hotkey_mapping.classes import Key
from utils.consts import load_env

load_env()

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
sorted(devices, key=lambda device: device.path)
MOUSE_INPUTS = []
KEYBOARD_INPUTS = []
for device in devices:
    capabilities = device.capabilities(verbose=True)
    if ("EV_ABS", 3) in capabilities.keys():
        MOUSE_INPUTS.append(device)
    elif (
        ("EV_KEY", 1) in capabilities.keys()
        and ("KEY_LEFTALT", 56) in capabilities[("EV_KEY", 1)]
        and ("KEY_Q", 16) in capabilities[("EV_KEY", 1)]
    ):
        KEYBOARD_INPUTS.append(device)
        # print(device.path, device.name, device.phys, device.capabilities(verbose=True))
print("mice")
for device in MOUSE_INPUTS:
    print(
        device.path,
        device.name,
        device.phys,
        device.capabilities(verbose=True),
    )
print("keyboards")
for device in KEYBOARD_INPUTS:
    print(
        device.path,
        device.name,
        device.phys,
        device.capabilities(verbose=True),
    )


# exit()


def get_input_device(path: str) -> InputDevice:
    return InputDevice(path)


KEYBOARD_INPUT = get_input_device(os.environ["KEYBOARD_DEVICE_PATH"])
MOUSE_INPUT = get_input_device(os.environ["MOUSE_DEVICE_PATH"])

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
