from unittest.mock import MagicMock

from _pytest.monkeypatch import MonkeyPatch
from evdev import KeyEvent, UInput
from evdev import ecodes as e

import linux_hotkey.service as service
from linux_hotkey.classes import Key, Shortcut
from linux_hotkey.service import handle_key_event


def test_handle_key_event_remaps_control_p(monkeypatch: MonkeyPatch):
    mock_action = MagicMock()
    monkeypatch.setattr(service, "SHORTCUTS", [Shortcut(Key(e.KEY_P), mock_action, (Key(e.KEY_LEFTCTRL),))])
    virtual_device = MagicMock(__class__=UInput)
    assert (
        handle_key_event(virtual_device, MagicMock(scancode="KEY_LEFTCTRL", __class__=KeyEvent, keystate=0x1)) is False
    )
    assert handle_key_event(virtual_device, MagicMock(scancode="KEY_P", __class__=KeyEvent)) is True
    assert (
        handle_key_event(virtual_device, MagicMock(scancode="KEY_LEFTCTRL", __class__=KeyEvent, keystate=0x0)) is False
    )
    mock_action.assert_called_with(virtual_device)


def test_handle_key_event_doesnt_trigger_shortcut_with_wrong_modifier(monkeypatch: MonkeyPatch):
    mock_action = MagicMock()
    monkeypatch.setattr(service, "SHORTCUTS", [Shortcut(Key(e.KEY_P), mock_action, (Key(e.KEY_LEFTCTRL),))])
    virtual_device = MagicMock(__class__=UInput)
    assert (
        handle_key_event(virtual_device, MagicMock(scancode="KEY_LEFTSHIFT", __class__=KeyEvent, keystate=0x1)) is False
    )
    assert handle_key_event(virtual_device, MagicMock(scancode="KEY_P", __class__=KeyEvent)) is False
    assert (
        handle_key_event(virtual_device, MagicMock(scancode="KEY_LEFTSHIFT", __class__=KeyEvent, keystate=0x0)) is False
    )
    mock_action.assert_not_called()
