from unittest.mock import MagicMock, patch

from _pytest.monkeypatch import MonkeyPatch
from evdev import InputEvent, KeyEvent, SynEvent, UInput
from evdev import ecodes as e

import linux_hotkey.service as service
from linux_hotkey.classes import Key, Shortcut
from linux_hotkey.service import handle_event, handle_key_event
from linux_hotkey.xdotool_wrapper import Window


@patch("linux_hotkey.service.get_active_window")
def test_handle_key_event_remaps_control_p(
    mock_get_active_window: MagicMock, monkeypatch: MonkeyPatch, mock_virtual_device: UInput | MagicMock
):
    mock_get_active_window.return_value = Window("123", "window_name")
    mock_action = MagicMock()
    monkeypatch.setattr(
        service,
        "KEYBOARD_SHORTCUTS",
        [
            Shortcut(
                source_key=Key(e.KEY_P),
                action=mock_action,
                modifier_keys=(Key(e.KEY_LEFTCTRL),),
                state_keys=(),
                window_name="window_name",
            )
        ],
    )
    assert (
        handle_key_event(mock_virtual_device, MagicMock(scancode="KEY_LEFTCTRL", __class__=KeyEvent, keystate=0x1))
        is False
    )
    assert handle_key_event(mock_virtual_device, MagicMock(scancode="KEY_P", __class__=KeyEvent, keystate=0x1)) is True
    assert (
        handle_key_event(mock_virtual_device, MagicMock(scancode="KEY_LEFTCTRL", __class__=KeyEvent, keystate=0x0))
        is False
    )
    mock_action.assert_called_with(mock_virtual_device)


@patch("linux_hotkey.service.get_active_window")
def test_handle_key_event_doesnt_trigger_shortcut_with_wrong_modifier(
    mock_get_active_window: MagicMock, monkeypatch: MonkeyPatch, mock_virtual_device: UInput | MagicMock
):
    mock_get_active_window.return_value = Window("123", "window_name")
    mock_action = MagicMock()
    monkeypatch.setattr(
        service, "KEYBOARD_SHORTCUTS", [Shortcut(Key(e.KEY_P), mock_action, (Key(e.KEY_LEFTCTRL),), (), "window_name")]
    )
    assert (
        handle_key_event(mock_virtual_device, MagicMock(scancode="KEY_LEFTSHIFT", __class__=KeyEvent, keystate=0x1))
        is False
    )
    assert handle_key_event(mock_virtual_device, MagicMock(scancode="KEY_P", __class__=KeyEvent)) is False
    assert (
        handle_key_event(mock_virtual_device, MagicMock(scancode="KEY_LEFTSHIFT", __class__=KeyEvent, keystate=0x0))
        is False
    )
    mock_action.assert_not_called()


def test_handle_key_event_doesnt_send_hold(mock_virtual_device: UInput | MagicMock):
    assert (
        handle_key_event(mock_virtual_device, MagicMock(scancode="KEY_LEFTSHIFT", __class__=KeyEvent, keystate=0x2))
        is True
    )
    mock_virtual_device.syn.assert_not_called()


@patch("linux_hotkey.service.handle_key_event")
@patch("linux_hotkey.service.categorize")
def test_handle_event_only_sends_syn_when_on_other_non_remapped_event(
    mock_categorize: MagicMock, mock_handle_key_event: MagicMock, mock_virtual_device: UInput | MagicMock
):
    mock_handle_key_event.return_value = False
    mock_key_event = MagicMock(__class__=InputEvent)
    mock_categorize.return_value = MagicMock(__class__=KeyEvent)
    handle_event(mock_virtual_device, mock_key_event)
    mock_categorize.return_value = MagicMock(__class__=SynEvent)
    handle_event(mock_virtual_device, MagicMock(__class__=InputEvent))
    mock_virtual_device.write_event.assert_called_once_with(mock_key_event)
    mock_virtual_device.syn.assert_called_once()


@patch("linux_hotkey.service.handle_key_event")
@patch("linux_hotkey.service.categorize")
def test_handle_event_skips_if_remapped(
    mock_categorize: MagicMock, mock_handle_key_event: MagicMock, mock_virtual_device: UInput | MagicMock
):
    mock_handle_key_event.return_value = True
    mock_key_event = MagicMock(__class__=InputEvent)
    mock_categorize.return_value = MagicMock(__class__=KeyEvent)
    handle_event(mock_virtual_device, mock_key_event)
    mock_virtual_device.write_event.assert_not_called()
    mock_virtual_device.syn.assert_not_called()
