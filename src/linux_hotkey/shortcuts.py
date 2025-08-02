from collections.abc import Sequence
from functools import partial

from evdev import UInput
from evdev import ecodes as e

from general_utils.log_utils import logger
from linux_hotkey.classes import Key, KeyEventAction, Shortcut


def ctrl_p_action(virtual_device: UInput) -> bool:
    key_code = e.KEY_A
    write_key(virtual_device, key_code)
    return True


def poe_mouse_wheel_click(virtual_device: UInput) -> bool:
    click_mouse(virtual_device)
    return True


def poe_send_command(virtual_device: UInput, command: str) -> bool:
    logger.info(f"Running poe command: {command}")
    write_key(virtual_device, e.KEY_ENTER)
    virtual_device.write(e.EV_KEY, e.KEY_LEFTCTRL, KeyEventAction.DOWN)
    write_key(virtual_device, e.KEY_A)
    virtual_device.write(e.EV_KEY, e.KEY_LEFTCTRL, KeyEventAction.UP)
    write_letters(virtual_device, command)
    write_key(virtual_device, e.KEY_ENTER)
    return True


poe_send_hideout = partial(poe_send_command, command="/hideout")
poe_send_kingsmarch = partial(poe_send_command, command="/kingsmarch")
poe_send_thanks = partial(poe_send_command, command="Thank you!")


def write_key(virtual_device: UInput, key_code: int, wrapper_key_codes: Sequence[int] = ()):
    for wrapper_key_code in wrapper_key_codes:
        virtual_device.write(e.EV_KEY, wrapper_key_code, KeyEventAction.DOWN)
    virtual_device.write(e.EV_KEY, key_code, KeyEventAction.DOWN)
    virtual_device.write(e.EV_KEY, key_code, KeyEventAction.UP)
    for wrapper_key_code in reversed(wrapper_key_codes):
        virtual_device.write(e.EV_KEY, wrapper_key_code, KeyEventAction.UP)
    virtual_device.syn()


def click_mouse(virtual_device: UInput) -> bool:
    virtual_device.write(e.EV_REL, e.BTN_LEFT, KeyEventAction.DOWN)
    virtual_device.write(e.EV_REL, e.BTN_LEFT, KeyEventAction.UP)
    virtual_device.syn()
    return True


def write_letters(virtual_device: UInput, letters: str):
    for letter in letters:
        write_letter(virtual_device, letter)


def write_letter(virtual_device: UInput, letter: str):
    special_map = {
        "/": "KEY_SLASH",
        "\\": "KEY_BACKSLASH",
        "-": "KEY_MINUS",
        "=": "KEY_EQUAL",
        " ": "KEY_SPACE",
    }

    top_row_map = {
        "!": "1",
        "@": "2",
        "#": "3",
        "$": "4",
        "%": "5",
        "^": "6",
        "&": "7",
        "*": "8",
        "(": "9",
        ")": "0",
        "_": "-",
        "+": "=",
    }

    wrapping_key_codes = []
    if letter.upper() == letter and letter.isalpha():
        wrapping_key_codes = [
            e.KEY_LEFTSHIFT,
        ]
    if letter in top_row_map.keys():
        wrapping_key_codes = [
            e.KEY_LEFTSHIFT,
        ]
        letter = top_row_map[letter]
    key = special_map.get(letter)
    if not key:
        key = f"KEY_{letter}".upper()
    write_key(virtual_device, e.ecodes[key], wrapping_key_codes)


KEYBOARD_SHORTCUTS = [
    Shortcut(Key(e.KEY_P), ctrl_p_action, (Key(e.KEY_LEFTCTRL),)),
    Shortcut(
        Key(
            e.KEY_F5,
        ),
        poe_send_hideout,
        (),
        (),
        "Path of Exile",
    ),
    Shortcut(
        Key(
            e.KEY_F7,
        ),
        poe_send_kingsmarch,
        (),
        (),
        "Path of Exile",
    ),
    Shortcut(
        Key(
            e.KEY_F4,
        ),
        poe_send_thanks,
        (),
        (),
        "Path of Exile",
    ),
]

MOUSE_SHORTCUTS = [
    Shortcut(Key(e.REL_HWHEEL), poe_mouse_wheel_click, (Key(e.KEY_LEFTCTRL),), (), "Path of Exile"),
]
