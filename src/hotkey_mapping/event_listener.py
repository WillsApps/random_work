import asyncio
import os

from src.hotkey_mapping.utils import get_key_state
from src.utils.consts import load_env

try:
    from evdev import InputDevice, InputEvent, KeyEvent, categorize
    from evdev import ecodes as e
except ModuleNotFoundError:
    exit(0)


load_env()

modifier_keys = {
    e.KEY_LEFTCTRL: False,
    e.KEY_LEFTSHIFT: False,
    e.KEY_LEFTALT: False,
    e.KEY_RIGHTCTRL: False,
    e.KEY_RIGHTSHIFT: False,
    e.KEY_RIGHTALT: False,
}

state_keys = {
    e.KEY_NUMLOCK: False,
    e.KEY_CAPSLOCK: False,
}


def handle_key_event(dev: InputDevice, key_event: KeyEvent):
    # key up
    if key_event.keycode in state_keys.keys():
        state_keys[key_event.keycode] = get_key_state(dev, key_event.keycode)
        return
    if key_event.keystate == 0:
        # modifier key up
        if key_event.keycode in modifier_keys.keys():
            modifier_keys[key_event.keycode] = False
        return
    # key down
    # modifier key down
    if key_event.keycode in modifier_keys.keys():
        modifier_keys[key_event.keycode] = True
        return

    key = key_event.keycode[4:]

    dict2 = {"Z": "Y", "Y": "Z"}
    if key in dict2:
        key = dict2[key]

    if modifier_keys[e.KEY_LEFTSHIFT] or modifier_keys[e.KEY_RIGHTSHIFT]:
        top_row_dict = {
            "0": "=",
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
        modifiers.update({key: val for key, val in mod_dicts.items() if val})
    print(f"{key}, {modifiers}")


async def main():
    keyboard_device = InputDevice(os.environ["KEYBOARD_DEVICE_PATH"])
    for key in state_keys.keys():
        state_keys[key] = get_key_state(keyboard_device, key)
    async for event in keyboard_device.async_read_loop():
        key_event = categorize(event)
        if isinstance(key_event, KeyEvent):
            handle_key_event(keyboard_device, key_event)


if __name__ == "__main__":
    asyncio.run(main())
