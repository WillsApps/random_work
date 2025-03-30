import asyncio
import os

from utils.consts import load_env

try:
    from evdev import InputDevice, InputEvent, KeyEvent, categorize
    from evdev import ecodes as e
except ModuleNotFoundError:
    exit(0)

load_env()
KEYBOARD_INPUT = InputDevice(os.environ["KEYBOARD_DEVICE_PATH"])
