import asyncio
import os
import sys

from hotkey_mapping.utils import get_led_name

try:
    from evdev import InputDevice, KeyEvent, categorize
except ModuleNotFoundError:
    exit(0)

sys.path.append("/home/aggy/Code/random_work")
from src.utils.consts import load_env

load_env()

modifier_keys = {
    "KEY_LEFTCTRL": False,
    "KEY_LEFTSHIFT": False,
    "KEY_LEFTALT": False,
    "KEY_RIGHTCTRL": False,
    "KEY_RIGHTSHIFT": False,
    "KEY_RIGHTALT": False,
}

state_keys = {
    "KEY_NUMLOCK": False,
    "KEY_CAPSLOCK": False,
}


def get_key_state(_dev: InputDevice, key_code: str) -> bool:
    led_name = get_led_name(key_code)
    for name, _ in _dev.leds(True):
        if name == led_name:
            return True
    return False


async def main(_dev: InputDevice):
    async for event in _dev.async_read_loop():
        key_event = categorize(event)
        if isinstance(key_event, KeyEvent):
            # key up
            if key_event.keycode in state_keys.keys():
                state_keys[key_event.keycode] = get_key_state(_dev, key_event.keycode)
                continue
            if key_event.keystate == 0:
                # modifier key up
                if key_event.keycode in modifier_keys.keys():
                    modifier_keys[key_event.keycode] = False
                    continue
            # key down
            if key_event.keystate == 1:
                # modifier key down
                if key_event.keycode in modifier_keys.keys():
                    modifier_keys[key_event.keycode] = True
                    continue

                key = key_event.keycode[4:]

                dict2 = {"Z": "Y", "Y": "Z"}
                if key in dict2:
                    key = dict2[key]

                if modifier_keys["KEY_LEFTSHIFT"] or modifier_keys["KEY_RIGHTSHIFT"]:
                    top_row_dict = {
                        "0": "=",
                        "1": "!",
                        "2": '"',
                        "3": "§",
                        "4": "$",
                        "5": "%",
                        "6": "&",
                        "7": "/",
                        "8": "(",
                        "9": ")",
                    }
                    if key in top_row_dict:
                        key = top_row_dict[key]
                    else:
                        key = key.lower()
                else:
                    key = key.lower()
                modifiers = {}
                for mod_dicts in [modifier_keys, state_keys]:
                    modifiers.update(
                        {key: val for key, val in mod_dicts.items() if val}
                    )
                print(f"{key}, {modifiers}")


if __name__ == "__main__":
    dev = InputDevice(os.environ["KEYBOARD_DEVICE_PATH"])
    asyncio.run(main(dev))
