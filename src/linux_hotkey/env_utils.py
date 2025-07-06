from typing import Callable

from evdev import ecodes as e

from general_utils.log_utils import logger
from linux_hotkey.classes import Key
from linux_hotkey.settings import KEYBOARD_INPUT, MODIFIER_KEYS


def get_key(func: Callable) -> Callable:
    def inner(key: Key | int | str, *args, **kwargs):
        if not isinstance(key, Key):
            key = Key(key)
        return func(key, *args, **kwargs)

    return inner


@get_key
def get_key_state(key: Key) -> bool:
    logger.debug(f"{key.led_name=}")
    for name, _ in KEYBOARD_INPUT.leds(True):
        logger.debug(f"{name=}")
        if name == key.led_name:
            return True
    return False


def is_shift_down() -> bool:
    return MODIFIER_KEYS[Key(e.KEY_LEFTSHIFT)] or MODIFIER_KEYS[Key(e.KEY_RIGHTSHIFT)]
