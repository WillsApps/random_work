import subprocess
from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class Position(DataClassJsonMixin):
    x: int
    y: int


@dataclass
class Window(DataClassJsonMixin):
    id: str
    name: str


def run_command(command_parts: list[str]) -> str:
    return subprocess.check_output(command_parts).decode("utf-8")


def get_location() -> Position:
    # x:4003 y:266 screen:0 window:216006732
    output = run_command(["xdotool", "getmouselocation"])
    parts = output.split(" ")
    x = int(parts[0].split(":")[1])
    y = int(parts[1].split(":")[1])
    return Position(x=x, y=y)


def get_active_window() -> Window:
    # x:4003 y:266 screen:0 window:216006732
    output = run_command(["xdotool", "getmouselocation"])
    parts = output.split(" ")
    _id = parts[3].split(":")[1]
    name = run_command(["xdotool", "getwindowname", _id]).strip()
    return Window(id=_id, name=name)
