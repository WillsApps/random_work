import asyncio
import os
from typing import Any

from src.hotkey_mapping.utils import get_led_key, get_key_state
from src.utils.consts import load_env

try:
    from evdev import InputDevice, KeyEvent, categorize
except ModuleNotFoundError:
    InputDevice, KeyEvent, categorize = Any, Any, Any

state = {
    "flasks_running": False
}
tasks = []
def start_flasks(_dev: InputDevice):
    if not get_key_state(_dev, "KEY_CAPSLOCK"):
        return
    state["flasks_running"] = True


def stop_flasks(_dev: InputDevice):
    for task in tasks:
