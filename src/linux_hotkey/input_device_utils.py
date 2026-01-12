import re
import subprocess
import sys

from evdev import InputDevice

from general_utils.log_utils import logger
from linux_hotkey.classes import InputType

INPUT_NAME_MAP = {
    # InputType.MOUSE: "Logitech_Gaming_Mouse_G600",
    InputType.MOUSE: "Logitech_USB_Receiver",
    InputType.KEYBOARD: "Logitech_USB_Receiver",
    # InputType.KEYBOARD: "Corsair_CORSAIR_K70_RGB_PRO_Mechanical_Gaming_Keyboard",
}


def get_devices_by_id() -> list[str]:
    # Get the path to the input devices. These are dynamic, and can change on system reboot.
    devices_by_id = subprocess.run(["ls", "-l", "/dev/input/by-id"], encoding="utf-8", stdout=subprocess.PIPE)
    devices_by_id = devices_by_id.stdout.split("\n")
    [logger.info(device) for device in devices_by_id]

    return devices_by_id


def get_input_device(event_type: InputType) -> InputDevice:
    input_path = "/dev/input/"
    input_regex = f"^.*{INPUT_NAME_MAP[event_type]}.*event-{event_type}.*"
    devices_by_id = get_devices_by_id()
    for device_id in devices_by_id:
        device_match = re.search(input_regex, device_id)
        if device_match:
            input_path = input_path + re.search("event[0-9]{1,}", device_match.group()).group()
    if input_path == "/dev/input/" or not input_path:
        sys.exit(f"Devices {event_type} not found")
    return InputDevice(input_path)
