from typing import Any

try:
    from evdev import KEY, InputDevice, KeyEvent, categorize
    from evdev.ecodes import ecodes as ed
except ModuleNotFoundError:
    InputDevice, KeyEvent, categorize = Any, Any, Any


def get_key_name(key_code: int) -> str:
    return KEY[key_code]


def get_key_code(key_name: str) -> int:
    return ed[key_name]


def get_led_key(key_code: int) -> int:
    name = KEY[key_code]
    return ed[name.replace("KEY", "LED")[0:-3]]


def get_key_state(_dev: InputDevice, key_code: int) -> bool:
    led_name = get_led_key(key_code)
    for name, _ in _dev.leds(True):
        if name == led_name:
            return True
    return False
