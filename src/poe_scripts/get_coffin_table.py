import os
import re
from dataclasses import dataclass

from dotenv import load_dotenv
from pathlib import Path
from os import environ
import pandas

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

CSV_FOLDER = Path(environ["COFFIN_CSV_FOLDER"])
ORIGINAL_FILE = Path(environ["OBSIDIAN_PATH"]) / "PoE.md"
BACKUP_FILE = Path(environ["OBSIDIAN_PATH"]) / "BackupPoE.md"


PERCENT_REGEX = re.compile(r"(\d\d\d)%")

# 100% increased chance of Caster Modifiers - 1


@dataclass
class Modifier:
    name: str
    increase_quantity: float
    scarcer_quantity: float


def get_modifier_name(name: str) -> str:
    return name.split(" Modifier")[0].split(" ")[-1]


def get_percent(name: str) -> int:
    return int(PERCENT_REGEX.findall(name)[0])

def get_rows_newest_file(csv_folder: Path) -> list[dict[str, any]]:
    exports = [file for file in csv_folder.iterdir() if "Wealthy-Exile-export" in file.name]
    exports.sort(key=os.path.getctime, reverse=True)
    file = exports[0]
    return pandas.read_csv(file).to_dict(orient="records")


def get_modifiers(csv_data: list[dict]) -> dict[str,Modifier]:
    modifiers = {}
    for row in csv_data:
        name = row["Name"]
        if (
            "% increased chance of " not in name
            and "scarcer" not in name
            and "+50 to Modifier Tier" not in name
        ):
            continue
        if "+50 to Modifier Tier" in name:
            modifier_name = "Modifier Tier"
            percent = 0
        else:
            modifier_name = get_modifier_name(name)
            percent = get_percent(name)
        modifier = modifiers.get(modifier_name, Modifier(modifier_name, 0, 0))
        if percent == 100:
            modifier_change = 0.3
        elif percent == 200:
            modifier_change = 0.4
        else:
            modifier_change = 1
        if "% increased chance of " in name or "+50 to Modifier Tier" in name:
            modifier.increase_quantity += modifier_change * int(row["Quantity"])
        elif "scarcer" in name:
            modifier.scarcer_quantity += modifier_change * int(row["Quantity"])
        modifiers[modifier_name] = modifier
    return modifiers

def get_markdown_table(modifiers: dict[str,Modifier]) -> list[str]:
    table_lines = [
        (
            """|               | Increased | Scarcer |
    | ------------- | --------- | ------- |"""
        )
    ]
    for modifier in sorted(modifiers.values(), key=lambda x: x.name):
        if modifier.name == "Modifier Tier":
            continue
        table_lines.append(
            f"| {modifier.name:13} | {modifier.increase_quantity:9} | {modifier.scarcer_quantity:7} |"
        )
    tier_modifier = modifiers["Modifier Tier"]
    table_lines.append(
        f"| {tier_modifier.name:13} | {tier_modifier.increase_quantity:9} | {' ':7} |"
    )
    return table_lines

def make_backup(original_file: Path, backup_file: Path):
    with open(original_file, "r") as original_f:
        with open(backup_file, "w") as backup_f:
            backup_f.write(original_f.read())
def get_content_lines(original_file: Path) -> list[str]:
    with open(original_file, "r") as original_f:
        return original_f.read().split("\n")

def splice_in_rows(new_lines: list[str], original_lines: list[str],start_line: str, end_line: str, ) -> list[str]:
    start_line_number = 0
    end_line_number = 0
    for line_number, line in enumerate(original_lines):
        if line == start_line:
            start_line_number = line_number
        elif line == end_line:
            end_line_number = line_number

    return (
        original_lines[: start_line_number + 2] + new_lines + original_lines[end_line_number - 1 :]
    )

def write_content_lines(target_file: Path, content: list[str]):
    with open(target_file, "w") as f:
        f.write("\n".join(new_content))


if __name__ == '__main__':
    rows = get_rows_newest_file(CSV_FOLDER)
    modifiers = get_modifiers(rows)
    markdown_table = get_markdown_table(modifiers)
    original_content = get_content_lines(ORIGINAL_FILE)
    make_backup(ORIGINAL_FILE, BACKUP_FILE)
    new_content = splice_in_rows(markdown_table,original_content, "-- Table Start", "-- Table End", )
    write_content_lines(ORIGINAL_FILE, new_content)
