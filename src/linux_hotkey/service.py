import asyncio
import logging

from evdev import InputEvent, KeyEvent, RelEvent, SynEvent, UInput, categorize

from general_utils.log_utils import logger
from linux_hotkey.classes import InputType, Key, MyInputType
from linux_hotkey.modifier_utils import reset_key_states
from linux_hotkey.settings import INPUT_DEVICES, MODIFIER_KEYS, STATE_KEYS
from linux_hotkey.shortcuts import KEYBOARD_SHORTCUTS, MOUSE_SHORTCUTS
from linux_hotkey.xdotool_wrapper import get_active_window


async def remap_input(input_type: InputType):
    """Service loop for input.

    1. Creates virtual device
    2. Resets key states (capslock, numlock) every event to keep them always up to date
    """
    virtual_device_name = f"python-{input_type}-device"
    input_device = INPUT_DEVICES[input_type]
    virtual_device = MyInputType.from_device(input_device, name=virtual_device_name)
    reset_key_states()
    try:
        input_device.grab()
        async for event in input_device.async_read_loop():
            handle_event(virtual_device, event)
    finally:
        input_device.ungrab()


def handle_event(virtual_device: UInput, event: InputEvent):
    categorized = categorize(event)
    remapped = False

    if isinstance(categorized, KeyEvent):
        remapped = handle_key_event(virtual_device, categorized)
    elif isinstance(categorized, RelEvent):
        remapped = handle_rel_event(virtual_device, categorized)
    if remapped:
        return

    if not isinstance(categorized, SynEvent):
        virtual_device.write_event(event)
        virtual_device.syn()


def handle_key_event(virtual_device: UInput, key_event: KeyEvent) -> bool:
    """Handles key events.

    1. Checks if is one of the MONITORS_KEY (shift, control, ...)
    2. Runs through shortcuts to see if any are hit

    returns:
        True: if the event should not be written to the virtual device.
        False: if the event should be written to the virtual device.
    """
    reset_key_states()
    key = Key(key_event)
    if key in MODIFIER_KEYS:
        if key_event.keystate == KeyEvent.key_up:
            MODIFIER_KEYS[key] = False
            return False
        elif key_event.keystate == KeyEvent.key_down:
            MODIFIER_KEYS[key] = True
            return False
        elif key_event.keystate == KeyEvent.key_hold:
            # Hold - no need to keep sending the signal
            return True
    if key in STATE_KEYS:
        return False
    if key_event.keystate != KeyEvent.key_down:
        return False
    active_window = get_active_window()
    for shortcut in KEYBOARD_SHORTCUTS:
        if key != shortcut.source_key:
            continue
        if not all(MODIFIER_KEYS[modifier] for modifier in shortcut.modifier_keys):
            continue
        if not all(STATE_KEYS[modifier] for modifier in shortcut.state_keys):
            continue
        if not shortcut.window_name or shortcut.window_name.lower() != active_window.name.lower():
            continue
        shortcut.action(virtual_device)
        return True
    return False


def handle_rel_event(virtual_device: UInput, rel_event: RelEvent) -> bool:
    logger.debug(f"{rel_event}")
    logger.debug(f"{rel_event.event}")
    key = Key(rel_event)
    shortcut_found = False
    active_window = get_active_window()
    for shortcut in MOUSE_SHORTCUTS:
        if key != shortcut.source_key:
            continue
        if not all(MODIFIER_KEYS[modifier] for modifier in shortcut.modifier_keys):
            continue
        if not all(STATE_KEYS[modifier] for modifier in shortcut.state_keys):
            continue
        if not shortcut.window_name or shortcut.window_name.lower() != active_window.name.lower():
            continue
        shortcut.action(virtual_device)
        shortcut_found = True
    if not shortcut_found:
        virtual_device.write_event(rel_event.event)
        virtual_device.syn()
    return True


def main():
    logger.setLevel(logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # asyncio.ensure_future(remap_input(InputType.MOUSE))
    asyncio.ensure_future(remap_input(InputType.KEYBOARD))
    loop.run_forever()
