import subprocess
import time
from dataclasses import dataclass
from typing import Any

from dataclasses_json import DataClassJsonMixin

from utils.log_utils import logger


@dataclass
class Vector2(DataClassJsonMixin):
    x: float | int
    y: float | int

    def __sub__(self, other: Any):
        return Vector2(self.x - other.x, self.y - other.y)

    def __add__(self, other: Any):
        return Vector2(self.x + other.x, self.y + other.y)

    @property
    def magnitude(self) -> float:
        return abs(self.x + self.y / 2)

    def __divmod__(self, other: Any):
        return Vector2(float(self.x) / other.x, float(self.y) / other.y)

    def lerp(self, target: Any, percent: float):
        difference = target - self

        return Vector2(
            self.x + round(difference.x * percent),
            self.y + round(difference.y * percent),
        )


@dataclass
class Window(DataClassJsonMixin):
    id: str
    name: str


def run_command(command_parts: list[str]) -> str:
    logger.debug(command_parts)
    return subprocess.check_output(command_parts).decode("utf-8")


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


def move_mouse(
    target: Vector2,
    screens_per_second: float = 4,
    chunks_per_second: int = 100,
) -> None:
    start_time = time.time()
    start = get_mouse_location()
    logger.debug(start)
    logger.debug(target)
    duration = get_duration(start, target, screens_per_second)
    number_chunks = int(duration * chunks_per_second)
    logger.debug(f"{duration=}")
    logger.debug(f"{number_chunks=}")
    for i in range(number_chunks):
        percent = float(i) / number_chunks
        lerped = start.lerp(target, percent)
        run_command(["xdotool", "mousemove", f"{lerped.x}", f"{lerped.y}"])
        time.sleep(duration / number_chunks)
        # run_command(["xdotool", "sleep", f"{duration/number_chunks}"])
    run_command(["xdotool", "mousemove", f"{target.x}", f"{target.y}"])
    end_time = time.time()
    logger.debug(start_time)
    logger.debug(end_time)
    actual_duration = end_time - start_time
    logger.debug(f"{actual_duration=}")
    logger.debug(f"expected_duration={duration}")


def get_duration(start: Vector2, target: Vector2, screens_per_second: float):
    direction = target - start
    distance = direction.magnitude
    percent_of_screen = distance / get_display_size().magnitude
    logger.debug(f"{get_display_size().magnitude=}")
    logger.debug(f"{distance=}")
    logger.debug(f"{percent_of_screen=}")
    duration = percent_of_screen / screens_per_second
    return duration
