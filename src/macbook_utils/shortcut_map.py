import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Any, Set, Dict

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
    new_modifier: str
    key_names: List[str]
    key_type: str
    _optionals: Set[str] = field(default_factory=lambda: set())
    conditions: List[Condition] = field(default_factory=lambda: list())
    _clean_optionals: Set[str] = None

    @property
    def optionals(self):
        if not self._clean_optionals:
            self._clean_optionals = self._optionals
            try:
                self._clean_optionals.remove(self.original_modifier)
            except:
                pass
        return self._clean_optionals

    def to_dict(self) -> List[Dict[str, Any]]:
        rules = []
        for key in self.key_names:
            rule = {
                "description": f"{self.original_modifier} to {self.new_modifier} for {key}",
                "manipulators": [
                    {
                        "from": {
                            self.key_type: key.lower(),
                            "modifiers": {"mandatory": [self.new_modifier]},
                        },
                        "to": [
                            {
                                self.key_type: key.lower(),
                                "modifiers": [self.original_modifier],
                            }
                        ],
                        "type": "basic",
                    }
                ],
            }
            if self.optionals:
                rule["manipulators"][0]["from"]["modifiers"]["optional"] = list(
                    self.optionals
                )
            if self.conditions:
                rule["manipulators"][0]["conditions"] = [
                    condition.to_dict() for condition in self.conditions
                ]
            rules.append(rule)
        return rules


optionals = {"left_command", "left_control", "left_option", "left_shift"}


SHORTCUTS = [
    Shortcut(
        original_modifier="left_command",
        new_modifier="left_control",
        key_names=[
            "button1",
            "button2",
        ],
        key_type="pointing_button",
        _optionals=optionals,
        conditions=[
            Condition(
                "frontmost_application_if",
                "bundle_identifiers",
                ["com.jetbrains.pycharm.ce", "com.jetbrains.AppCode"],
            )
        ],
    ),
    Shortcut(
        original_modifier="left_command",
        new_modifier="left_control",
        key_names=[
            "a",
            "x",
            "q",
            "z",
            "t",
            "w",
            "r",
            "f",
            "c",
            "v",
            "i",
            "p",
            "i",
            "1",
            "2",
            "3",
            "4",
            "5",
        ],
        key_type="key_code",
        _optionals=optionals,
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
    Shortcut(
        original_modifier="left_option",
        new_modifier="left_control",
        key_names=[
            "delete_or_backspace",
            "right_arrow",
            "left_arrow",
        ],
        key_type="key_code",
        _optionals=optionals,
    ),
    Shortcut(
        original_modifier="left_command",
        new_modifier="left_option",
        key_names=[
            "grave_accent_and_tilde",
            "tab",
        ],
        key_type="key_code",
        _optionals={"left_shift"},
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
