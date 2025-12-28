from collections.abc import Callable, Iterable
from dataclasses import dataclass
from enum import IntEnum, StrEnum

from beartype.typing import Any, Optional
from evdev import KeyEvent, RelEvent, UInput
from evdev.ecodes import ecodes as key_str_dict
from evdev.ecodes import keys as key_int_dict


class InputType(StrEnum):
    MOUSE = "mouse"
    KEYBOARD = "kbd"


class KeyEventAction(IntEnum):
    UP = 0
    DOWN = 1
    HOLD = 2


class MyInputType(UInput):
    def write_event(self, event):
        super().write_event(event)


class Key:
    def __init__(self, scan_code_or_name: int | str | KeyEvent | RelEvent):
        try:
            if isinstance(scan_code_or_name, KeyEvent):
                scan_code_or_name = scan_code_or_name.scancode
            elif isinstance(scan_code_or_name, RelEvent):
                scan_code_or_name = scan_code_or_name.event.code
            if isinstance(scan_code_or_name, int):
                self.code = scan_code_or_name
                name = key_int_dict[self.code]
                self.name = name[0] if isinstance(name, tuple) else name
            elif isinstance(scan_code_or_name, str):
                self.name = scan_code_or_name
                self.code = key_str_dict[self.name]
        except KeyError:
            print(scan_code_or_name)
            raise
        self.value = self.name[4:]

    def __str__(self):
        return f"Key({self.name=}, {self.code=})"

    def __repr__(self):
        return f"Key({self.name=}, {self.code=})"

    @property
    def led_name(self) -> str:
        return self.name.replace("KEY", "LED")[0:-3]

    def __hash__(self) -> int:
        return self.code

    def __eq__(self, other: Any) -> bool:
        return self.code == other.code


@dataclass
class Shortcut:
    source_key: Key
    action: Callable[[UInput], bool]
    modifier_keys: Iterable[Key] = ()
    state_keys: Iterable[Key] = ()
    window_name: Optional[str] = None
