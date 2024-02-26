import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Any, Set, Dict, Union


# @dataclass
# class Shortcut:
#     description: str
#     key_code: str
#     new_modifier: str
#     original_modifier: str
#     optional_modifiers: List[str] = field(default=lambda: [])
#
#     def to_dict(self):
#         return {
#             "description": self.description,
#             "type": "basic",
#             "manipulators": [
#                 {
#                     "from": {
#                         "key_code": self.key_code,
#                         "modifiers": {"mandatory": [self.original_modifier]},
#                     },
#                     "to": [
#                         {"key_code": self.key_code, "modifiers": [self.new_modifier]}
#                     ],
#                 }
#             ],
#         }


class KeyCodes(Enum):
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


class PointingButtons(Enum):
    TYPE = "pointing_button"
    LEFT_CLICK = "button1"
    RIGHT_CLICK = "button2"
    MIDDLE_CLICK = "button3"


KeyType = Union[KeyCodes, PointingButtons]


@dataclass()
class Condition:
    type: str
    option_1_name: str
    option_1_value: any

    def to_dict(self) -> Dict[str, any]:
        return {"type": self.type, self.option_1_name: self.option_1_value}


@dataclass()
class Shortcut:
    original_modifier: str
    optionals: Set[str]

    def __post_init__(self):
        self.cleaned_optionals: Set[str] = self.get_cleaned_optionals()

    def get_cleaned_optionals(self):
        cleaned_optionals = self.optionals
        if self.original_modifier in cleaned_optionals:
            cleaned_optionals.remove(self.original_modifier)
        return cleaned_optionals


@dataclass()
class KeyChangeShortcut(Shortcut):
    original_key: KeyType
    new_key: KeyType
    new_modifier: str = None
    conditions: List[Condition] = field(default_factory=lambda: list())

    def to_dict(self) -> List[Dict[str, Any]]:
        rules = []
        part_from = {
            self.original_key.TYPE.value: self.original_key.value,
        }
        if self.original_modifier:
            part_from["modifiers"] = {"mandatory": [self.original_modifier]}

        part_to = {
            self.new_key.TYPE.value: self.new_key.value.lower(),
        }
        if self.new_modifier:
            part_to["modifiers"] = {"mandatory": [self.new_modifier]}
        rule = {
            "description": f"{self.original_modifier}+{self.original_key} to {self.new_modifier}+{self.new_key}",
            "manipulators": [
                {
                    "from": part_from,
                    "to": [part_to],
                    "type": "basic",
                }
            ],
        }
        if self.cleaned_optionals:
            rule["manipulators"][0]["from"]["modifiers"]["optional"] = list(
                self.cleaned_optionals
            )
        if self.conditions:
            rule["manipulators"][0]["conditions"] = [
                condition.to_dict() for condition in self.conditions
            ]
        rules.append(rule)
        return rules


@dataclass()
class ModifierChangeShortcut(Shortcut):
    new_modifier: str
    keys: List[KeyType]
    conditions: List[Condition] = field(default_factory=lambda: list())

    def to_dict(self) -> List[Dict[str, Any]]:
        rules = []
        for key in self.keys:
            rule = {
                "description": f"{self.original_modifier} to {self.new_modifier} for {key.value}",
                "manipulators": [
                    {
                        "from": {
                            key.TYPE.value: key.value,
                            "modifiers": {"mandatory": [self.new_modifier]},
                        },
                        "to": [
                            {
                                key.TYPE.value: key.value,
                                "modifiers": [self.original_modifier],
                            }
                        ],
                        "type": "basic",
                    }
                ],
            }
            if self.cleaned_optionals:
                rule["manipulators"][0]["from"]["modifiers"]["optional"] = list(
                    self.cleaned_optionals
                )
            if self.conditions:
                rule["manipulators"][0]["conditions"] = [
                    condition.to_dict() for condition in self.conditions
                ]
            rules.append(rule)
        return rules


optionals = {"left_command", "left_control", "left_option", "left_shift"}


SHORTCUTS = [
    # ModifierChangeShortcut(
    #     original_modifier="left_command",
    #     new_modifier="left_control",
    #     key_names=[
    #         "button1",
    #         "button2",
    #     ],
    #     key_type="pointing_button",
    #     optionals=optionals,
    #     conditions=[
    #         Condition(
    #             "frontmost_application_if",
    #             "bundle_identifiers",
    #             ["com.jetbrains.pycharm.ce", "com.jetbrains.AppCode"],
    #         )
    #     ],
    # ),
    # KeyChangeShortcut(
    #     original_modifier="left_control",
    #     original_key="button1",
    #     original_key_type="pointing_button",
    #     new_modifier="left_control",
    #     new_key="button3",
    #     new_key_type="pointing_button",
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
        original_modifier="left_command",
        new_modifier="left_control",
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
        optionals=optionals,
        conditions=[
            Condition(
                "frontmost_application_unless",
                "bundle_identifiers",
                [
                    "com.jetbrains.pycharm.ce",
                    "com.jetbrains.AppCode",
                    "com.googlecode.iterm2",
                ],
            )
        ],
    ),
    ModifierChangeShortcut(
        original_modifier="left_option",
        new_modifier="left_control",
        keys=[
            KeyCodes.DELETE_OR_BACKSPACE,
            KeyCodes.RIGHT_ARROW,
            KeyCodes.LEFT_ARROW,
        ],
        optionals=optionals,
    ),
    ModifierChangeShortcut(
        original_modifier="left_command",
        new_modifier="left_option",
        keys=[
            KeyCodes.GRAVE_ACCENT_AND_TILDE,
            KeyCodes.TAB,
        ],
        optionals={"left_shift"},
    ),
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
        f.write(json.dumps(raw, indent=2))
    print(json.dumps(rules))


if __name__ == "__main__":
    main()
