def get_led_name(key_code: str) -> str:
    return key_code.replace("KEY", "LED")[0:-3]
