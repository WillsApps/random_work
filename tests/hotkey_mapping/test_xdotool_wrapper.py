from unittest.mock import MagicMock, patch

from hotkey_mapping.xdotool_wrapper import (
    Vector2,
    Window,
    get_active_window,
    get_display_size,
    get_mouse_location,
    move_mouse,
)


@patch("hotkey_mapping.xdotool_wrapper.run_command")
def test_get_mouse_location(mock_run_command: MagicMock) -> None:
    mock_run_command.return_value = "x:4003 y:266 screen:0 window:216006732"
    expected = Vector2(x=4003, y=266)
    actual = get_mouse_location()
    assert actual == expected


@patch("hotkey_mapping.xdotool_wrapper.run_command")
def test_get_display_size(mock_run_command: MagicMock) -> None:
    mock_run_command.return_value = "123 1200"
    expected = Vector2(x=123, y=1200)
    actual = get_display_size()
    assert actual == expected


@patch("hotkey_mapping.xdotool_wrapper.run_command")
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


# @patch("hotkey_mapping.xdotool_wrapper.run_command")
def test_move_mouse():
    move_mouse(Vector2(1000, 1000))
