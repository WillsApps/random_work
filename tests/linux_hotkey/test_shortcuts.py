from unittest.mock import MagicMock, patch

import pytest
from evdev import UInput
from evdev import ecodes as e

from linux_hotkey.classes import KeyEventAction
from linux_hotkey.shortcuts import write_key, write_letter


def test_write_key_no_wrapping_key_codes(mock_virtual_device: UInput | MagicMock):
    mock_key_code = MagicMock(spec=int)
    write_key(mock_virtual_device, mock_key_code)
    all_calls = mock_virtual_device.write.call_args_list
    assert len(all_calls) == 2
    assert all_calls[0][0] == (e.EV_KEY, mock_key_code, KeyEventAction.DOWN)
    assert all_calls[1][0] == (e.EV_KEY, mock_key_code, KeyEventAction.UP)
    mock_virtual_device.syn.assert_called_once()


def test_write_key_has_wrapping_key_codes(mock_virtual_device: UInput | MagicMock):
    wrapper_key_codes = (
        e.KEY_LEFTCTRL,
        e.KEY_LEFTSHIFT,
    )
    mock_key_code = MagicMock(spec=int)
    write_key(mock_virtual_device, mock_key_code, wrapper_key_codes)
    all_calls = mock_virtual_device.write.call_args_list
    assert len(all_calls) == 6

    assert all_calls[0][0] == (e.EV_KEY, e.KEY_LEFTCTRL, KeyEventAction.DOWN)
    assert all_calls[1][0] == (e.EV_KEY, e.KEY_LEFTSHIFT, KeyEventAction.DOWN)
    assert all_calls[2][0] == (e.EV_KEY, mock_key_code, KeyEventAction.DOWN)
    assert all_calls[3][0] == (e.EV_KEY, mock_key_code, KeyEventAction.UP)
    assert all_calls[4][0] == (e.EV_KEY, e.KEY_LEFTSHIFT, KeyEventAction.UP)
    assert all_calls[5][0] == (e.EV_KEY, e.KEY_LEFTCTRL, KeyEventAction.UP)
    mock_virtual_device.syn.assert_called_once()


@patch("linux_hotkey.shortcuts.write_key")
@pytest.mark.parametrize(
    "example_letter,expected_keycode",
    [
        (
            "a",
            e.KEY_A,
        ),
        ("/", e.KEY_SLASH),
    ],
)
def test_write_letter_no_modifiers(
    mock_write_key: MagicMock, example_letter: str, expected_keycode: int, mock_virtual_device: UInput | MagicMock
):
    write_letter(mock_virtual_device, example_letter)
    mock_write_key.assert_called_once_with(mock_virtual_device, expected_keycode, [])


@patch("linux_hotkey.shortcuts.write_key")
@pytest.mark.parametrize(
    "example_letter,expected_keycode,expected_modifiers",
    [
        (
            "A",
            e.KEY_A,
            [
                e.KEY_LEFTSHIFT,
            ],
        ),
        (
            "+",
            e.KEY_EQUAL,
            [
                e.KEY_LEFTSHIFT,
            ],
        ),
    ],
)
def test_write_letter_has_modifiers(
    mock_write_key: MagicMock,
    example_letter: str,
    expected_keycode: int,
    expected_modifiers: list[int],
    mock_virtual_device: UInput | MagicMock,
):
    write_letter(mock_virtual_device, example_letter)
    mock_write_key.assert_called_once_with(mock_virtual_device, expected_keycode, expected_modifiers)
