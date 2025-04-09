from evdev import UInput
from evdev import ecodes as e

from hotkey_mapping.classes import Key
from hotkey_mapping.settings import KEYBOARD_INPUT, MOUSE_INPUT, MOUSE_INPUTS


def send_key(key: Key):
    with UInput.from_device(KEYBOARD_INPUT) as writer:
        writer.write(e.EV_KEY, key.code, 1)
        writer.write(e.EV_KEY, key.code, 0)
        writer.syn()


def send_click():
    with UInput.from_device(MOUSE_INPUT) as ui:
        ui.write(e.EV_KEY, e.BTN_MOUSE, 1)
        ui.write(e.EV_KEY, e.BTN_MOUSE, 0)
        ui.syn()


def move_mouse(x: int, y: int):
    print(f"mouse_move, {x}, {y}")
    # cap = {
    #     e.EV_KEY: [e.KEY_A, e.KEY_B],
    #     e.EV_ABS: [
    #         (
    #             e.ABS_X,
    #             AbsInfo(value=0, min=0, max=255, fuzz=0, flat=0, resolution=0),
    #         ),
    #         (e.ABS_Y, AbsInfo(0, 0, 255, 0, 0, 0)),
    #         (e.ABS_MT_POSITION_X, (0, 128, 255, 0)),
    #     ],
    # }
    # ui = UInput(
    #     {
    #         e.EV_KEY: [e.KEY_A, e.KEY_B],
    #         e.EV_REL: [e.REL_X, e.REL_Y],
    #         e.EV_ABS: [
    #             (
    #                 e.ABS_X,
    #                 AbsInfo(value=0, min=0, max=255, fuzz=0, flat=0, resolution=0),
    #             ),
    #             (e.ABS_Y, AbsInfo(0, 0, 255, 0, 0, 0)),
    #             (e.ABS_MT_POSITION_X, (0, 128, 255, 0)),
    #         ],
    #     }
    # )
    ui = UInput.from_device(MOUSE_INPUTS[1])
    # with UInput.from_device(MOUSE_INPUT) as ui:
    print(ui)
    print(ui.capabilities(verbose=True))
    ui.syn()
    # ui.write(e.EV_REL, e.REL_X, x)
    # ui.write(e.EV_REL, e.REL_Y, y)
    ui.write(e.EV_KEY, e.BTN_LEFT, 0)
    ui.write(e.EV_KEY, e.BTN_LEFT, 1)
    # ui.syn()
    # ui.write(e.EV_ABS, e.ABS_X, 20)
    # ui.write(e.EV_ABS, e.ABS_Y, 20)
    ui.syn()
    ui.close()
