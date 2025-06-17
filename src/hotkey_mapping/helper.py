import os

import evdev
from evdev import InputDevice

from general_utils.consts import load_env

load_env()
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
devices.append(InputDevice(os.environ["KEYBOARD_DEVICE_PATH"]))

for device in sorted(devices, key=lambda d: d.path):
    print(f"'{device.path}', '{device.name}', '{device.capabilities(verbose=True)}'")
