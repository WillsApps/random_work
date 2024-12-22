import os
import re
from dataclasses import dataclass
from os import environ
from pathlib import Path

import pandas
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

CSV_FOLDER = Path(environ["COFFIN_CSV_FOLDER"])
ORIGINAL_FILE = Path(environ["OBSIDIAN_PATH"]) / "PoE.md"
BACKUP_FILE = Path(environ["OBSIDIAN_PATH"]) / "BackupPoE.md"


PERCENT_REGEX = re.compile(r"(\d){2,3}%")

# 100% increased chance of Caster Modifiers - 1


@dataclass
class Modifier:
    name: str
    increase_quantity: float
    scarcer_quantity: float
    is_meta: bool


def get_modifier_name(row: str) -> str:
    return row.split(" Modifier")[0].split(" ")[-1]


def get_percent(row: str) -> int:
    return int(PERCENT_REGEX.findall(row)[0])


def get_rows_newest_file(csv_folder: Path) -> list[dict[str, any]]:
    exports = [
        file for file in csv_folder.iterdir() if "Wealthy-Exile-export" in file.name
    ]
    exports.sort(key=os.path.getctime, reverse=True)
    file = exports[0]
    return pandas.read_csv(file).to_dict(orient="records")


def get_name_percent_and_is_meta(row: str) -> tuple[str, int, bool]:
    name_map = {
        "+50 to Modifier Tier": lambda n: "Modifier Tier",
        "Reroll Modifier": lambda n: "Reroll Explicit",
        "Reroll Implicit": lambda n: "Reroll Implicit",
        "Corruption": lambda n: "Corruption",
        "Randomized": lambda n: "Randomized",
        "Fracture": lambda n: "Fracture",
        "Grave Row": lambda n: "Grave Row",
        "Grave Column": lambda n: "Grave Column",
        "40% increased Effect": lambda n: (
            "Effect of " + n.split("40% increased Effect of ")[1].split(" ")[0]
        ),
    }

    for key, name_func in name_map.items():
        if key in row:
            return name_func(row), 0, True
    return get_modifier_name(row), get_percent(row), False


def get_modifiers(csv_data: list[dict]) -> dict[str, Modifier]:
    modifiers = {}
    for full_row in csv_data:
        row = full_row["Name"]
        if (
            "% increased chance of " not in row
            and "% increased chance for " not in row
            and "scarcer" not in row
            and "+50 to Modifier Tier" not in row
            and "Randomized" not in row
            and "chance to Fracture" not in row
            and "40% increased Effect" not in row
            and "Grave Row" not in row
            and "Grave Column" not in row
            and "Reroll" not in row
        ):
            continue
        modifier_name, percent, is_meta = get_name_percent_and_is_meta(row)
        #
        # for key, name_func in name_map.items():
        #     if key in row:
        #         modifier_name, percent = name_func(row)
        #         break
        # if "+50 to Modifier Tier" in row:
        #     modifier_name, percent = name_map["+50 to Modifier Tier"](row)
        #     percent = 0
        # elif "40% increased Effect" in row:
        #     modifier_name, percent = name_map["40% increased Effect"](row)
        #     modifier_name = (
        #         "Effect of " + row.split("40% increased Effect of ")[1].split(" ")[0]
        #     )
        #     percent = 0
        # elif "Reroll Modifier" in row:
        #     modifier_name = "Reroll Explicit"
        #     percent = 0
        # elif "Reroll Implicit" in row:
        #     modifier_name = "Reroll Implicit"
        #     percent = 0
        # else:
        #     modifier_name = get_modifier_name(row)
        #     percent = get_percent(row)
        modifier = modifiers.get(modifier_name, Modifier(modifier_name, 0, 0, is_meta))
        if percent == 100:
            modifier_change = 0.3
        elif percent == 200:
            modifier_change = 0.4
        else:
            modifier_change = 1
        if "scarcer" in row:
            modifier.scarcer_quantity += modifier_change * int(full_row["Quantity"])
        else:
            modifier.increase_quantity += modifier_change * int(full_row["Quantity"])
        modifiers[modifier_name] = modifier
    return modifiers


def get_markdown_table(modifiers: dict[str, Modifier]) -> list[str]:
    table_lines = [
        (
            """| Name          | Increased | Scarcer |
    | ------------- | --------- | ------- |"""
        )
    ]
    for modifier in sorted(modifiers.values(), key=lambda x: x.name):
        if modifier.is_meta:
            continue
        table_lines.append(
            f"| {modifier.name:13} | {modifier.increase_quantity:9} | {modifier.scarcer_quantity:7} |"
        )

    table_lines.append("")
    table_lines.append(
        (
            """| Name          | Count |
    | ------------- | ----- |"""
        )
    )
    for modifier in sorted(modifiers.values(), key=lambda x: x.name):
        if not modifier.is_meta:
            continue
        table_lines.append(f"| {modifier.name:13} | {modifier.increase_quantity:5} |")
    # tier_modifier = modifiers["Modifier Tier"]
    # table_lines.append(
    #     f"| {tier_modifier.name:13} | {tier_modifier.increase_quantity:9} | {' ':7} |"
    # )
    return table_lines


def make_backup(original_file: Path, backup_file: Path):
    with open(original_file, "r") as original_f:
        with open(backup_file, "w") as backup_f:
            backup_f.write(original_f.read())


def get_content_lines(original_file: Path) -> list[str]:
    with open(original_file, "r") as original_f:
        return original_f.read().split("\n")


def splice_in_rows(
    new_lines: list[str],
    original_lines: list[str],
    start_line: str,
    end_line: str,
) -> list[str]:
    start_line_number = 0
    end_line_number = 0
    for line_number, line in enumerate(original_lines):
        if line == start_line:
            start_line_number = line_number
        elif line == end_line:
            end_line_number = line_number

    return (
        original_lines[: start_line_number + 2]
        + new_lines
        + original_lines[end_line_number - 1 :]
    )


def write_content_lines(target_file: Path, content: list[str]):
    with open(target_file, "w") as f:
        f.write("\n".join(content))


def main():
    rows = get_rows_newest_file(CSV_FOLDER)
    modifiers = get_modifiers(rows)
    markdown_table = get_markdown_table(modifiers)
    # meta_markdown_table = get_markdown_table(meta_modifiers)
    original_content = get_content_lines(ORIGINAL_FILE)
    make_backup(ORIGINAL_FILE, BACKUP_FILE)
    new_content = splice_in_rows(
        markdown_table,
        original_content,
        "-- Table Start",
        "-- Table End",
    )
    write_content_lines(ORIGINAL_FILE, new_content)


if __name__ == "__main__":
    main()
