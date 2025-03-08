from src.hotkey_mapping.keyboard_listener import get_led_name


def test_get_led_name():
    key_code = "KEY_NUMLOCK"
    expected = "LED_NUML"
    actual = get_led_name(key_code)
    assert actual == expected
