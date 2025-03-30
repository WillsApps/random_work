from hotkey_mapping.env_utils import get_led_key


def test_get_led_name():
    key_code = "KEY_NUMLOCK"
    expected = "LED_NUML"
    actual = get_led_key(key_code)
    assert actual == expected
