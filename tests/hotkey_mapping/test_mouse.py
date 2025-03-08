from unittest.mock import MagicMock, patch

from src.hotkey_mapping.mouse import Position, Window, get_active_window, get_location


@patch("src.hotkey_mapping.mouse.run_command")
def test_get_location(mock_run_command: MagicMock) -> None:
    mock_run_command.return_value = "x:4003 y:266 screen:0 window:216006732"
    expected = Position(x=4003, y=266)
    actual = get_location()
    assert actual == expected


@patch("src.hotkey_mapping.mouse.run_command")
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
