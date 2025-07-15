from linux_hotkey.classes import Key


def test_led_name():
    assert Key("KEY_NUMLOCK").led_name == "LED_NUML"
    assert Key("KEY_CAPSLOCK").led_name == "LED_CAPSL"
