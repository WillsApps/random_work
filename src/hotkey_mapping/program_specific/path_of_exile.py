import asyncio
from typing import Any, Callable

from hotkey_mapping.env_utils import Key, get_key_state

try:
    from evdev import InputDevice, KeyEvent, categorize
    from evdev import ecodes as e
except ModuleNotFoundError:
    InputDevice, KeyEvent, categorize = Any, Any, Any

state = {"flasks_running": False}
tasks = []


def start_flasks(_dev: InputDevice):
    if not get_key_state(_dev, e.KEY_CAPSLOCK):
        return
    state["flasks_running"] = True


# def stop_flasks(_dev: InputDevice):
#     for task in tasks:


# helper function for running a target periodically
async def periodic(interval_sec: float, coro_name: Callable, *args, **kwargs):
    # loop forever
    while state["flasks_running"]:
        # await the target
        await coro_name(*args, **kwargs)
        # wait an interval
        await asyncio.sleep(interval_sec)


# general task
async def send_key(key: Key):
    # report a message
    print(f"Sending {key}")


# main coroutine
async def main():
    # report a message
    print("Main starting")
    # configure the periodic task
    t1 = asyncio.create_task(periodic(1.0, send_key, Key(4)))
    t2 = asyncio.create_task(periodic(1.0, send_key, Key(6)))
    await t1
    await t2
    print("Main done")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
