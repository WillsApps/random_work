from typing import Any

from hotkey_mapping.globals import KEYBOARD_INPUT
from utils.log_utils import logger

try:
    from evdev import InputDevice, KeyEvent, categorize
    from evdev.ecodes import ecodes as key_str_dict
    from evdev.ecodes import KEY as KEY_INT_DICT
except ModuleNotFoundError:
    InputDevice, KeyEvent, categorize = Any, Any, Any


class Key:
    def __init__(self, key: int | str):
        self.code = get_key_code(key)
        self.name = get_key_name(key)
        self.value = self.name[4:]

    def __str__(self):
        return f"Key({self.name=}, {self.code=})"

    @property
    def led_name(self) -> str:
        return self.name.replace("KEY", "LED")[0:-3]


def get_key_name(key_code: int) -> str:
    if isinstance(key_code, str):
        return key_code
    return KEY_INT_DICT[key_code]


def get_key_code(key_name: str) -> int:
    if isinstance(key_name, int):
        return key_name
    return key_str_dict[key_name]


def get_led_key(key: int | str) -> str:
    if isinstance(key, int):
        key = get_key_name(key)
    return key.replace("KEY", "LED")[0:-3]


def get_key_state(key: Key) -> bool:
    logger.debug(f"{key.led_name=}")
    for name, _ in KEYBOARD_INPUT.leds(True):
        logger.debug(f"{name=}")
        if name == key.led_name:
            return True
    return False
