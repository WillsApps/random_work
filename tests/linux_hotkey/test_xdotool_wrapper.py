from typing import NamedTuple
from unittest.mock import MagicMock, call, patch

import pytest

from linux_hotkey.xdotool_wrapper import (
    Vector2,
    Window,
    get_active_window,
    get_display_size,
    get_duration,
    get_mouse_location,
    move_mouse,
    normalize_target,
)


@patch("linux_hotkey.xdotool_wrapper.run_command")
def test_get_mouse_location(mock_run_command: MagicMock) -> None:
    mock_run_command.return_value = "x:4003 y:266 screen:0 window:216006732"
    expected = Vector2(x=4003.0, y=266.0)
    actual = get_mouse_location()
    assert actual == expected


@patch("linux_hotkey.xdotool_wrapper.run_command")
def test_get_display_size(mock_run_command: MagicMock) -> None:
    mock_run_command.return_value = "123 1200"
    expected = Vector2(x=123.0, y=1200.0)
    actual = get_display_size()
    assert actual == expected


@patch("linux_hotkey.xdotool_wrapper.run_command")
def test_get_active_window(mock_run_command: MagicMock) -> None:
    def side_effect(command_parts: list[str]) -> str:
        return {
            "getmouselocation": "x:4003 y:266 screen:0 window:216006732",
            "getwindowname": "the name",
        }[command_parts[1]]

    mock_run_command.side_effect = side_effect
    expected = Window(id="216006732", name="the name")
    actual = get_active_window()
    assert actual == expected


@patch("linux_hotkey.xdotool_wrapper.get_display_size")
def test_normalize_target_primary_screen_doesnt_change_anything(
    mock_get_display_size: MagicMock,
):
    mock_get_display_size.return_value = Vector2(2560.0, 1440.0)
    start = Vector2(1000.0, 1000.0)
    target = Vector2(2000.0, 1200.0)
    expected = target
    actual = normalize_target(start, target)
    assert actual == expected


@patch("linux_hotkey.xdotool_wrapper.get_display_size")
def test_normalize_target_second_screen_changes_just_x(
    mock_get_display_size: MagicMock,
):
    mock_get_display_size.return_value = Vector2(2400.0, 1440.0)
    start = Vector2(2500.0, 1000.0)
    target = Vector2(2000.0, 1200.0)
    expected = Vector2(4400.0, 1200.0)
    actual = normalize_target(start, target)
    assert actual == expected


ParamGetDuration = NamedTuple(
    "ParamGetDuration",
    (
        ("start", Vector2),
        ("target", Vector2),
        ("screens_per_second", float),
        ("display_size", Vector2),
        ("expected", float),
    ),
)


@pytest.mark.parametrize(
    ParamGetDuration._fields,
    [
        # Happy Path
        ParamGetDuration(
            start=Vector2(0.0, 0.0),
            target=Vector2(500.0, 500.0),
            screens_per_second=1.0,
            display_size=Vector2(1000.0, 1000.0),
            expected=0.5,
        ),
        # Moving to smaller target
        ParamGetDuration(
            start=Vector2(500.0, 500.0),
            target=Vector2(0.0, 0.0),
            screens_per_second=1.0,
            display_size=Vector2(1000.0, 1000.0),
            expected=0.5,
        ),
        # Further than display size
        ParamGetDuration(
            start=Vector2(0.0, 0.0),
            target=Vector2(500.0, 500.0),
            screens_per_second=1.0,
            display_size=Vector2(250.0, 250.0),
            expected=2,
        ),
        # Higher screens per second
        ParamGetDuration(
            start=Vector2(0.0, 0.0),
            target=Vector2(500.0, 500.0),
            screens_per_second=10.0,
            display_size=Vector2(1000.0, 1000.0),
            expected=0.05,
        ),
        # Lower screens per second
        ParamGetDuration(
            start=Vector2(0.0, 0.0),
            target=Vector2(500.0, 500.0),
            screens_per_second=0.1,
            display_size=Vector2(1000.0, 1000.0),
            expected=5,
        ),
        # Super not rounded
        ParamGetDuration(
            start=Vector2(321.0, 654.0),
            target=Vector2(123.0, 456.0),
            screens_per_second=0.33,
            display_size=Vector2(777.0, 999.0),
            expected=0.6704580248065322,
        ),
    ],
)
@patch("linux_hotkey.xdotool_wrapper.get_display_size")
def test_get_duration(
    mock_get_display_size: MagicMock,
    start: Vector2,
    target: Vector2,
    screens_per_second: float,
    display_size: Vector2,
    expected: float,
):
    mock_get_display_size.return_value = display_size
    actual = get_duration(start, target, screens_per_second)
    assert_within_margin_of_error(actual, expected)


def assert_within_margin_of_error(actual: Vector2 | float, expected: Vector2 | float):
    """Asserting floats ya know?"""
    margin_of_error = 0.000001
    if isinstance(actual, Vector2):
        margin_of_error = Vector2(margin_of_error, margin_of_error)
    assert expected - margin_of_error < actual < expected + margin_of_error


ParamVector2Magnitude = NamedTuple(
    "TestVector2Lerp",
    (
        ("x", float),
        ("y", float),
        ("expected", float),
    ),
)


@pytest.mark.parametrize(
    ParamVector2Magnitude._fields,
    [
        ParamVector2Magnitude(x=3.0, y=4.0, expected=5),
        ParamVector2Magnitude(x=33.0, y=44.0, expected=55),
        ParamVector2Magnitude(x=3.0, y=3.0, expected=4.242640),
    ],
)
def test_Vector2_magnitude(x: float, y: float, expected: float):
    actual = Vector2(x, y).magnitude
    assert_within_margin_of_error(actual, expected)


ParamVector2Lerp = NamedTuple(
    "ParamVector2Lerp",
    (
        ("start", Vector2),
        ("target", Vector2),
        ("percent", float),
        ("expected", Vector2),
    ),
)


@pytest.mark.parametrize(
    ParamVector2Lerp._fields,
    [
        ParamVector2Lerp(
            start=Vector2(0.0, 0.0),
            target=Vector2(1.0, 1.0),
            percent=0.5,
            expected=Vector2(0.5, 0.5),
        ),
        ParamVector2Lerp(
            start=Vector2(0.0, 0.0),
            target=Vector2(50.0, 100.0),
            percent=0.9,
            expected=Vector2(45.0, 90.0),
        ),
    ],
)
def test_Vector2_lerp(start: Vector2, target: Vector2, percent: float, expected: Vector2):
    actual = start.lerp(target, percent)
    assert_within_margin_of_error(actual, expected)


@patch("linux_hotkey.xdotool_wrapper.get_mouse_location")
@patch("linux_hotkey.xdotool_wrapper.normalize_target")
@patch("linux_hotkey.xdotool_wrapper.get_duration")
@patch("linux_hotkey.xdotool_wrapper.run_command")
@patch("linux_hotkey.xdotool_wrapper.time.sleep")
def test_move_mouse_has_right_number_of_calls(
    mock_sleep: MagicMock,
    mock_run_command: MagicMock,
    mock_get_duration: MagicMock,
    mock_normalize_target: MagicMock,
    mock_get_mouse_location: MagicMock,
):
    # 1 second, 4 chunks; so 5 run commands, 4 sleep commands
    mock_get_duration.return_value = 1
    mock_start = MagicMock()
    mock_target = MagicMock()
    mock_get_mouse_location.return_value = mock_start
    screens_per_second = 1
    chunks_per_second = 4
    move_mouse(
        target=mock_target,
        screens_per_second=screens_per_second,
        chunks_per_second=chunks_per_second,
    )
    mock_normalize_target.assert_called_with(mock_get_mouse_location.return_value, mock_target)
    mock_get_duration.assert_called_with(mock_start, mock_normalize_target.return_value, screens_per_second)
    assert mock_run_command.call_count == 5
    assert mock_sleep.call_count == 4
    assert mock_start.lerp.call_args_list == [
        call(
            mock_normalize_target.return_value,
            0.0,
        ),
        call(
            mock_normalize_target.return_value,
            0.25,
        ),
        call(
            mock_normalize_target.return_value,
            0.5,
        ),
        call(
            mock_normalize_target.return_value,
            0.75,
        ),
    ]
    assert mock_run_command.call_args_list[-1] == call(
        (
            "xdotool",
            "mousemove",
            f"{mock_normalize_target.return_value.x}",
            f"{mock_normalize_target.return_value.y}",
        ),
        False,
    )
