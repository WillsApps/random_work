import re
import sys
from select import select

from evdev import InputDevice, UInput, ecodes

from linux_hotkey.input_device_utils import get_devices_by_id


def main():
    virtual_device_name = "python-mouse-device"
    input_mouse = "/dev/input/"
    input_keyboard = "/dev/input/"

    # These Regex's may need to be updated per-device. These match
    # my Azeron Cyro Mouse and Key Inputs.
    keyboard_name = "Corsair_CORSAIR_K70_RGB_PRO_Mechanical_Gaming_Keyboard"
    mouse_name = "Logitech_Gaming_Mouse_G600"
    input_keyboard_regex = f"^.*{keyboard_name}.*event-kbd.*"
    input_mouse_regex = f"^.*{mouse_name}.*event-mouse.*"

    devices_by_id = get_devices_by_id()

    for device_id in devices_by_id:
        device_match = re.search(input_mouse_regex, device_id)
        if device_match:
            input_mouse = input_mouse + re.search("event[0-9]{1,}", device_match.group()).group()

        device_match = re.search(input_keyboard_regex, device_id)
        if device_match:
            input_keyboard = input_keyboard + re.search("event[0-9]{1,}", device_match.group()).group()

    if input_mouse == "/dev/input/" or not input_mouse:
        sys.exit("Mouse not found")

    if input_keyboard == "/dev/input/" or not input_keyboard:
        sys.exit("Keyboard not found")

    # Create the virtual mouse
    ui = UInput.from_device(InputDevice(input_mouse), name=virtual_device_name)

    try:
        # Define the devices
        devices = map(InputDevice, (input_keyboard, input_mouse))
        devices = {dev.fd: dev for dev in devices}
        # for dev in devices.values(): print(dev)

        # Grab the devices to block their native input
        for dev in devices.values():
            dev.grab()

        # Read and handle events from the devices and translate it to the virtual device
        r, w, x = select(devices, [], [])
        for fd in r:
            for event in devices[fd].read():
                if event.type == ecodes.EV_MSC and event.code == 4 and event.value == 458767:
                    print(event)  # remap or add a script to perform
                # Add more if / elif as needed for different keys or key combinations

                # If you didn't remap the key, pass the input through as normal
                ui.write(event.type, event.code, event.value)
    finally:
        for dev in devices.values():
            dev.ungrab()
