from evdev import ecodes as e

from linux_hotkey.classes import Key
from linux_hotkey.settings import KEYBOARD_INPUT, MODIFIER_KEYS, STATE_KEYS


def get_key_state(key: Key) -> bool:
    active_names = [name for name, _ in KEYBOARD_INPUT.leds(True)]
    if key.led_name in active_names:
        return True
    return False


def is_shift_down() -> bool:
    return MODIFIER_KEYS[Key(e.KEY_LEFTSHIFT)] or MODIFIER_KEYS[Key(e.KEY_RIGHTSHIFT)]


def reset_key_states() -> None:
    for key in STATE_KEYS.keys():
        STATE_KEYS[key] = get_key_state(key)
