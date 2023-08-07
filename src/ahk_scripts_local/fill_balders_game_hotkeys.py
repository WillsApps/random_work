from pathlib import Path

KEYS = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "-",
    "=",
]
MODIFIERS = [
    ("", ""),
    ("{Shift}", "+"),
    ("{Ctrl}", "^"),
    ("{Alt}", "!"),
]
SOURCE = Path(__file__).parent / "balders_game_source.ahk"
TARGET = Path(__file__).parent / "balders_game.ahk"
OFFSET = 59
TOP_X = 888
TOP_Y = 1164


def get_hotkey_template(key, x_pos, y_pos, modifier: tuple[str, str]):
    return f"""
    {modifier[1]}{key}::{{
        games_click_back({x_pos}, {y_pos}, "{modifier[0]}{key}")
    }}
"""


def get_lines():
    lines = []
    with open(SOURCE, "r") as f:
        source = f.read().split("\n")
    for line in source:
        lines.append(line)
        if "START_GEN_HERE" in line:
            return lines


def main():
    lines = get_lines()
    for row_level, modifier in enumerate(MODIFIERS):
        for key_index, key in enumerate(KEYS):
            x_pos = TOP_X + key_index * OFFSET
            y_pos = TOP_Y + row_level * OFFSET
            lines.append(get_hotkey_template(key, x_pos, y_pos, modifier))
    with open(TARGET, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
