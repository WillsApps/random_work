import asyncio

from evdev import InputEvent, KeyEvent, RelEvent, SynEvent, UInput, categorize

from linux_hotkey.classes import InputType, Key
from linux_hotkey.modifier_utils import reset_key_states
from linux_hotkey.settings import INPUT_DEVICES, MODIFIER_KEYS, STATE_KEYS
from linux_hotkey.shortcuts import SHORTCUTS
from linux_hotkey.xdotool_wrapper import get_active_window


async def remap_input(input_type: InputType):
    virtual_device_name = f"python-{input_type}-device"
    input_device = INPUT_DEVICES[input_type]
    virtual_device = UInput.from_device(input_device, name=virtual_device_name)
    reset_key_states()
    try:
        input_device.grab()
        async for event in input_device.async_read_loop():
            reset_key_states()
            handle_event(virtual_device, event)
    finally:
        input_device.ungrab()


def handle_event(virtual_device: UInput, event: InputEvent):
    categorized = categorize(event)
    if isinstance(categorized, SynEvent):
        virtual_device.syn()
        return
    remapped = False
    if isinstance(categorized, KeyEvent):
        remapped = handle_key_event(virtual_device, categorized)
    elif isinstance(categorized, RelEvent):
        remapped = handle_rel_event(virtual_device, categorized)
    if not remapped:
        virtual_device.write_event(event)
    virtual_device.syn()


def handle_key_event(virtual_device: UInput, key_event: KeyEvent) -> bool:
    key = Key(key_event)
    if key in MODIFIER_KEYS:
        if key_event.keystate == KeyEvent.key_up:
            MODIFIER_KEYS[key] = False
        else:
            MODIFIER_KEYS[key] = True
        return False
    if key in STATE_KEYS:
        return False
    active_window = get_active_window()
    for shortcut in SHORTCUTS:
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
    return False


if __name__ == "__main__":
    # logger.setLevel(logging.DEBUG)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # asyncio.ensure_future(remap_input(InputType.MOUSE))
    asyncio.ensure_future(remap_input(InputType.KEYBOARD))
    loop.run_forever()
