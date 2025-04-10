from typing import Any

from evdev.ecodes import ecodes as key_str_dict
from evdev.ecodes import keys as key_int_dict


class Key:
    def __init__(self, key: int | str):
        try:
            if isinstance(key, int):
                self.code = key
                name = key_int_dict[self.code]
                self.name = name[0] if isinstance(name, tuple) else name
            elif isinstance(key, str):
                self.name = key
                self.code = key_str_dict[self.name]
        except KeyError:
            print(key)
            raise
        self.value = self.name[4:]

    def __str__(self):
        return f"Key({self.name=}, {self.code=})"

    @property
    def led_name(self) -> str:
        return self.name.replace("KEY", "LED")[0:-3]

    def __hash__(self) -> int:
        return self.code

    def __eq__(self, other: Any) -> bool:
        return self.code == other.code
