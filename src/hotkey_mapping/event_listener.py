import asyncio

from evdev import KeyEvent, RelEvent, categorize

from general_utils.log_utils import logger
from hotkey_mapping.env_utils import Key, get_key_state, is_shift_down
from hotkey_mapping.event_writer import move_mouse, send_click, send_key
from hotkey_mapping.settings import (
    KEYBOARD_INPUT,
    MODIFIER_KEYS,
    MOUSE_INPUT,
    STATE_KEYS,
)


def key_up(key: Key):
    if key in MODIFIER_KEYS.keys():
        MODIFIER_KEYS[key] = False


def key_down(key: Key):
    logger.debug(f"{key=}")
    if key in STATE_KEYS.keys():
        STATE_KEYS[key] = get_key_state(key)
        return
    if key in MODIFIER_KEYS.keys():
        MODIFIER_KEYS[key] = True
        return
    key_output = key.value.lower()
    if key == Key("KEY_A"):
        move_mouse(20, 20)
        send_click()
        send_key(Key("KEY_B"))
    if is_shift_down():
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
    for mod_dicts in [MODIFIER_KEYS, STATE_KEYS]:
        modifiers.update({key.name: val for key, val in mod_dicts.items() if val})
    logger.debug(f"{key_output}, {modifiers=}")


def key_held(key: Key):
    pass


def mouse_up(key: Key):
    pass


def mouse_down(key: Key):
    log_key_press(key.value.lower())


def mouse_held(key: Key):
    pass


key_state_map = {
    0: key_up,
    1: key_down,
    2: key_held,
}

mouse_state_map = {
    0: mouse_up,
    1: mouse_down,
    2: mouse_held,
}


def handle_key_event(key_event: KeyEvent):
    key = Key(key_event.scancode)
    key_state_map[key_event.keystate](key)


def handle_mouse_event(key_event: KeyEvent):
    key = Key(key_event.scancode)
    mouse_state_map[key_event.keystate](key)


def reset_state_keys():
    for key in STATE_KEYS.keys():
        STATE_KEYS[key] = get_key_state(key)


async def keyboard():
    reset_state_keys()
    async for event in KEYBOARD_INPUT.async_read_loop():
        key_event = categorize(event)
        if isinstance(key_event, KeyEvent):
            handle_key_event(key_event)


async def mouse():
    async for event in MOUSE_INPUT.async_read_loop():
        key_event = categorize(event)
        if isinstance(key_event, KeyEvent):
            handle_key_event(key_event)
        elif isinstance(key_event, RelEvent):
            # This is a mouse movement
            # print(f"{key_event}, {key_event.event}")
            pass


if __name__ == "__main__":
    asyncio.ensure_future(keyboard())
    asyncio.ensure_future(mouse())
    loop = asyncio.get_event_loop()
    loop.run_forever()
