import asyncio
import os

from hotkey_mapping.globals import KEYBOARD_INPUT
from hotkey_mapping.env_utils import get_key_state, get_key_name, Key
from utils.consts import load_env
from utils.log_utils import logger

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


def key_up(key: Key):
    if key.code in modifier_keys.keys():
        modifier_keys[key.code] = False


def key_down(key: Key):
    logger.debug(f"{key=}")
    if key.code in state_keys.keys():
        state_keys[key.code] = get_key_state(key.code)
        return
    if key.code in modifier_keys.keys():
        modifier_keys[key.code] = True
        return
    key_output = key.value.lower()
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
        if key.value in top_row_dict:
            key_output = top_row_dict[key_output]
    log_key_press(key_output)


def log_key_press(key_output: str):
    modifiers = {}
    for mod_dicts in [modifier_keys, state_keys]:
        modifiers.update(
            {get_key_name(key): val for key, val in mod_dicts.items() if val}
        )
    logger.debug(f"{key_output}, {modifiers=}")


def key_held(key: Key):
    pass


key_state_map = {
    0: key_up,
    1: key_down,
    2: key_held,
}


def handle_key_event(key_event: KeyEvent):
    key = Key(key_event.scancode)
    key_state_map[key_event.keystate](key)

    dict2 = {"Z": "Y", "Y": "Z"}
    if key in dict2:
        key = dict2[key]


def reset_state_keys():
    for key in state_keys.keys():
        state_keys[key] = get_key_state(key)


async def main():
    reset_state_keys()
    async for event in KEYBOARD_INPUT.async_read_loop():
        key_event = categorize(event)
        if isinstance(key_event, KeyEvent):
            handle_key_event(key_event)


if __name__ == "__main__":
    asyncio.run(main())
