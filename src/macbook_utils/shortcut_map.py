import json
from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Any, Set, Dict, Union, Sequence


class KeyCodes(str, Enum):
    TYPE = "key_code"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    H = "h"
    I = "i"
    J = "j"
    K = "k"
    L = "l"
    M = "m"
    N = "n"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    S = "s"
    T = "t"
    U = "u"
    V = "v"
    W = "w"
    X = "x"
    Y = "y"
    Z = "z"
    N1 = "1"
    N2 = "2"
    N3 = "3"
    N4 = "4"
    N5 = "5"
    N6 = "6"
    N7 = "7"
    N8 = "8"
    N9 = "9"
    N0 = "0"
    DOWN_ARROW = "down_arrow"
    UP_ARROW = "up_arrow"
    LEFT_ARROW = "left_arrow"
    RIGHT_ARROW = "right_arrow"
    GRAVE_ACCENT_AND_TILDE = "grave_accent_and_tilde"
    TAB = "tab"
    DELETE_OR_BACKSPACE = "delete_or_backspace"


class PointingButtons(str, Enum):
    TYPE = "pointing_button"
    LEFT_CLICK = "button1"
    RIGHT_CLICK = "button2"
    MIDDLE_CLICK = "button3"


class ConsumerKeyCode(str, Enum):
    TYPE = "consumer_key_code"
    PLAY_OR_PAUSE = "play_or_pause"


class Modifiers(str, Enum):
    LEFT_CONTROL = "left_control"
    LEFT_SHIFT = "left_shift"
    LEFT_COMMAND = "left_command"
    LEFT_OPTION = "left_option"


KeyType = Union[KeyCodes, PointingButtons, ConsumerKeyCode]


def values_from_enum_list(enums: Sequence[Enum]):
    return [val.value for val in enums]


@dataclass()
class Condition:
    type: str
    option_1_name: str
    option_1_value: any

    def to_dict(self) -> Dict[str, any]:
        return {"type": self.type, self.option_1_name: self.option_1_value}


@dataclass()
class Shortcut:
    original_modifiers: List[Modifiers]
    optional_modifiers: List[Modifiers]
    conditions: List[Condition]

    def __post_init__(self):
        self.cleaned_optionals: List[Modifiers] = list(set(self.optional_modifiers) - set(self.original_modifiers))

    @staticmethod
    def get_part_direction(
        key: KeyType, direction: str, modifiers: Sequence[Modifiers] = ()
    ):
        part = {key.TYPE: key, "modifiers": {}}
        if modifiers:
            if direction == "from":
                part["modifiers"] = {"mandatory": values_from_enum_list(modifiers)}
            else:
                part["modifiers"] = values_from_enum_list(modifiers)
        return part

    def add_manipulators_optional(self, rule: Dict[str, Any]):
        if not self.cleaned_optionals:
            return
        rule["manipulators"][0]["from"]["modifiers"]["optional"] = (
            values_from_enum_list(self.cleaned_optionals)
        )

    def add_manipulators_conditional(self, rule: Dict[str, Any]):
        if not self.conditions:
            return
        rule["manipulators"][0]["conditions"] = [
            condition.to_dict() for condition in self.conditions
        ]


@dataclass()
class KeyChangeShortcut(Shortcut):
    original_key: KeyType
    new_key: KeyType
    new_modifiers: Sequence[Modifiers] = None

    def to_dict(self) -> List[Dict[str, Any]]:
        rule = {
            "description": f"{values_from_enum_list(self.original_modifiers)}+{self.original_key} to {values_from_enum_list(self.new_modifiers)}+{self.new_key}",
            "manipulators": [
                {
                    "from": Shortcut.get_part_direction(
                        self.original_key, "from", self.original_modifiers
                    ),
                    "to": [
                        Shortcut.get_part_direction(
                            self.new_key, "to", self.new_modifiers
                        )
                    ],
                    "type": "basic",
                }
            ],
        }
        self.add_manipulators_optional(rule)
        self.add_manipulators_conditional(rule)
        return [rule]


@dataclass()
class ModifierChangeShortcut(Shortcut):
    new_modifiers: Sequence[Modifiers]
    keys: List[KeyType]

    def to_dict(self) -> List[Dict[str, Any]]:
        rules = []
        for key in self.keys:
            rule = {
                "description": f"{values_from_enum_list(self.original_modifiers)} to {values_from_enum_list(self.new_modifiers)} for {key}",
                "manipulators": [
                    {
                        "from": Shortcut.get_part_direction(
                            key, "from", self.new_modifiers
                        ),
                        "to": [
                            Shortcut.get_part_direction(
                                key, "to", self.original_modifiers
                            )
                        ],
                        "type": "basic",
                    }
                ],
            }
            self.add_manipulators_optional(rule)
            self.add_manipulators_conditional(rule)
            rules.append(rule)
        return rules


@dataclass()
class DisableShortcut(Shortcut):
    keys: List[KeyType]

    def to_dict(self) -> List[Dict[str, Any]]:
        rules = []
        for key in self.keys:
            rule = {
                "description": f"Disabling {key}",
                "manipulators": [
                    {
                        "from": Shortcut.get_part_direction(
                            key, "from"
                        ),
                        "to": [
                        ],
                        "type": "basic",
                    }
                ],
            }
            self.add_manipulators_optional(rule)
            self.add_manipulators_conditional(rule)
            rules.append(rule)
        return rules


optional_modifiers = [
    Modifiers.LEFT_COMMAND,
    Modifiers.LEFT_CONTROL,
    Modifiers.LEFT_OPTION,
    Modifiers.LEFT_SHIFT,
]

SHORTCUTS = [
    # KeyChangeShortcut(
    #     original_modifier=Modifiers.LEFT_COMMAND,
    #     original_key=PointingButtons.LEFT_CLICK,
    #     new_modifier=Modifiers.LEFT_CONTROL,
    #     new_key=PointingButtons.RIGHT_CLICK,
    #     optionals=set(),
    #     conditions=[
    #         Condition(
    #             "frontmost_application_if",
    #             "bundle_identifiers",
    #             ["com.jetbrains.pycharm.ce", "com.jetbrains.AppCode"],
    #         )
    #     ],
    # ),
    ModifierChangeShortcut(
        original_modifiers=[Modifiers.LEFT_OPTION, Modifiers.LEFT_COMMAND, Modifiers.LEFT_OPTION],
        new_modifiers=[Modifiers.LEFT_COMMAND, Modifiers.LEFT_SHIFT],
        keys=[
            KeyCodes.V,
        ],
        optional_modifiers=[],
        conditions=[
            Condition(
                "frontmost_application_if",
                "bundle_identifiers",
                [
                    "com.jgraph.drawio.desktop",
                ],
            )
        ],
    ),
    ModifierChangeShortcut(
        original_modifiers=[Modifiers.LEFT_COMMAND],
        new_modifiers=[Modifiers.LEFT_SHIFT, Modifiers.LEFT_CONTROL],
        keys=[
            KeyCodes.C,
        ],
        optional_modifiers=[],
        conditions=[
            Condition(
                "frontmost_application_if",
                "bundle_identifiers",
                [
                    "com.google.Chrome",
                ],
            )
        ],
    ),
    ModifierChangeShortcut(
        original_modifiers=[Modifiers.LEFT_COMMAND],
        new_modifiers=[Modifiers.LEFT_CONTROL],
        keys=[
            KeyCodes.A,
            KeyCodes.X,
            KeyCodes.Q,
            KeyCodes.Z,
            KeyCodes.T,
            KeyCodes.W,
            KeyCodes.R,
            KeyCodes.F,
            KeyCodes.C,
            KeyCodes.V,
            KeyCodes.I,
            KeyCodes.P,
            KeyCodes.I,
            KeyCodes.N1,
            KeyCodes.N2,
            KeyCodes.N3,
            KeyCodes.N4,
            KeyCodes.N5,
        ],
        optional_modifiers=optional_modifiers,
        conditions=[
            Condition(
                "frontmost_application_unless",
                "bundle_identifiers",
                [
                    "com.jetbrains.pycharm.ce",
                    "com.jetbrains.pycharm",
                    "com.jetbrains.AppCode",
                    "com.googlecode.iterm2",
                ],
            )
        ],
    ),
    ModifierChangeShortcut(
        original_modifiers=[Modifiers.LEFT_OPTION],
        new_modifiers=[Modifiers.LEFT_CONTROL],
        keys=[
            KeyCodes.DELETE_OR_BACKSPACE,
            KeyCodes.RIGHT_ARROW,
            KeyCodes.LEFT_ARROW,
        ],
        optional_modifiers=optional_modifiers,
        conditions=[
            # Condition(
            #     "frontmost_application_unless",
            #     "bundle_identifiers",
            #     [
            #         "com.apple.finder",
            #     ],
            # )
        ],
    ),
    DisableShortcut(
        original_modifiers=[Modifiers.LEFT_OPTION],
        keys=[
            ConsumerKeyCode.PLAY_OR_PAUSE,
        ],
        optional_modifiers=optional_modifiers,
        conditions=[
            # Condition(
            #     "frontmost_application_unless",
            #     "bundle_identifiers",
            #     [
            #         "com.apple.finder",
            #     ],
            # )
        ],
    ),
    # ---- Replaced with "AltTab" ----
    # ModifierChangeShortcut(
    #     original_modifier=Modifiers.LEFT_COMMAND,
    #     new_modifier=Modifiers.LEFT_OPTION,
    #     keys=[
    #         KeyCodes.GRAVE_ACCENT_AND_TILDE,
    #         KeyCodes.TAB,
    #     ],
    #     optionals=[Modifiers.LEFT_SHIFT],
    #     conditions=[],
    # ),
]

root = Path("/Users/will.burdett/.config/karabiner")


def main():
    d = datetime.now()
    rules = []
    for shortcut in SHORTCUTS:
        rules.extend(shortcut.to_dict())
    with open(root / "karabiner.json", "r") as f:
        raw = json.loads(f.read())
    with open(
        root / f"karabiner_backup_{d.strftime('%Y_%m_%d_%H_%M')}.json",
        "w",
    ) as f:
        f.write(json.dumps(raw, indent=2))
    raw["profiles"][0]["complex_modifications"]["rules"] = rules
    with open(root / "karabiner.json", "w") as f:
        output = json.dumps(raw, indent=2)
        f.write(output)
    print(json.dumps(rules))


if __name__ == "__main__":
    main()
