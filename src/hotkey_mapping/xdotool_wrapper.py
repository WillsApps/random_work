import subprocess
import time
from collections.abc import Sequence
from dataclasses import dataclass
from math import sqrt
from typing import Any, Optional

from dataclasses_json import DataClassJsonMixin

from general_utils.log_utils import logger, timeit


@dataclass
class Vector2(DataClassJsonMixin):
    x: float
    y: float

    @property
    def magnitude(self) -> float:
        return sqrt((self.x * self.x) + (self.y * self.y))

    def lerp(self, target: Any, percent: float):
        if not isinstance(target, Vector2):
            raise NotImplementedError()
        difference = target - self

        return Vector2(
            self.x + (difference.x * percent),
            self.y + (difference.y * percent),
        )

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vector2):
            raise NotImplementedError()
        return self.magnitude < other.magnitude

    def __divmod__(self, other: Any):
        if not isinstance(other, Vector2):
            raise NotImplementedError()
        return Vector2(self.x / other.x, self.y / other.y)

    def __sub__(self, other: Any):
        return Vector2(self.x - other.x, self.y - other.y)

    def __add__(self, other: Any):
        return Vector2(self.x + other.x, self.y + other.y)


@dataclass
class Window(DataClassJsonMixin):
    id: str
    name: str


def run_command(command_parts: Sequence[str], grab_output: bool = True) -> Optional[str]:
    logger.debug(command_parts)
    if grab_output:
        return subprocess.check_output(command_parts).decode("utf-8")
    subprocess.run(command_parts)


def get_mouse_location() -> Vector2:
    # x:4003 y:266 screen:0 window:216006732
    output = run_command(["xdotool", "getmouselocation"])
    parts = output.split(" ")
    x = int(parts[0].split(":")[1])
    y = int(parts[1].split(":")[1])
    return Vector2(x=x, y=y)


def get_active_window() -> Window:
    # x:4003 y:266 screen:0 window:216006732
    output = run_command(["xdotool", "getmouselocation"])
    parts = output.split(" ")
    _id = parts[3].split(":")[1]
    name = run_command(["xdotool", "getwindowname", _id]).strip()
    return Window(id=_id, name=name)


def get_display_size() -> Vector2:
    output = run_command(["xdotool", "getdisplaygeometry"])
    parts = output.split(" ")
    x = int(parts[0])
    y = int(parts[1])
    return Vector2(x=x, y=y)


def normalize_target(start: Vector2, target: Vector2) -> Vector2:
    display_size = get_display_size()
    if start.x > display_size.x:
        return Vector2(target.x + display_size.x, target.y)
    return target


@timeit
def move_mouse(
    target: Vector2,
    screens_per_second: float = 4,
    chunks_per_second: int = 100,
) -> None:
    start = get_mouse_location()
    target = normalize_target(start, target)
    duration = get_duration(start, target, screens_per_second)
    number_chunks = int(duration * chunks_per_second)
    commands = []
    for i in range(number_chunks):
        percent = float(i) / number_chunks
        lerped = start.lerp(target, percent)
        commands.append(
            (
                run_command,
                (("xdotool", "mousemove", f"{lerped.x}", f"{lerped.y}"), False),
            )
        )
        commands.append((time.sleep, [duration / number_chunks]))
    commands.append((run_command, (("xdotool", "mousemove", f"{target.x}", f"{target.y}"), False)))
    for func, args in commands:
        func(*args)
    logger.debug(f"expected_duration={duration}")


def get_duration(start: Vector2, target: Vector2, screens_per_second: float):
    direction = target - start
    distance = direction.magnitude
    display_size = get_display_size()
    percent_of_screen = distance / display_size.magnitude
    duration = percent_of_screen / screens_per_second
    return duration
