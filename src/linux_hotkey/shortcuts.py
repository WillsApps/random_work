from functools import partial

from evdev import UInput
from evdev import ecodes as e

from linux_hotkey.classes import Key, KeyEventAction, Shortcut


def ctrl_p_action(virtual_device: UInput) -> bool:
    key_code = e.KEY_A
    write_key(virtual_device, key_code)
    return True


def poe_send_command(virtual_device: UInput, command: str) -> bool:
    write_key(virtual_device, e.KEY_ENTER)
    virtual_device.write(e.EV_KEY, e.KEY_LEFTCTRL, KeyEventAction.DOWN)
    write_key(virtual_device, e.KEY_A)
    virtual_device.write(e.EV_KEY, e.KEY_LEFTCTRL, KeyEventAction.UP)
    write_letters(virtual_device, command)
    write_key(virtual_device, e.KEY_ENTER)
    return True


poe_send_hideout = partial(poe_send_command, command="/hideout")
poe_send_kingsmarch = partial(poe_send_command, command="/kingsmarch")


def write_key(virtual_device: UInput, key_code: int):
    virtual_device.write(e.EV_KEY, key_code, KeyEventAction.DOWN)
    virtual_device.write(e.EV_KEY, key_code, KeyEventAction.UP)
    virtual_device.syn()


def write_keys(virtual_device: UInput, key_codes: list[int]):
    for key_code in key_codes:
        write_key(virtual_device, key_code)


def write_letters(virtual_device: UInput, letters: str):
    special_map = {
        "/": "KEY_SLASH",
        "\\": "KEY_BACKSLASH",
    }
    for letter in letters:
        key = special_map.get(letter)
        if not key:
            key = f"KEY_{letter}".upper()
        write_key(virtual_device, e.ecodes[key])


SHORTCUTS = [
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
]
