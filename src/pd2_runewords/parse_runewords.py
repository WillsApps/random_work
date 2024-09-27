import re
from dataclasses import dataclass
from typing import Dict, List

from bs4 import BeautifulSoup


RUNES = [
    "El",
    "Eld",
    "Tir",
    "Nef",
    "Eth",
    "Ith",
    "Tal",
    "Ral",
    "Ort",
    "Thul",
    "Amn",
    "Sol",
    "Shael",
    "Dol",
    "Hel",
    "Io",
    "Lum",
    "Ko",
    "Fal",
    "Lem",
    "Pul",
    "Um",
    "Mal",
    "Ist",
    "Gul",
    "Vex",
    "Ohm",
    "Lo",
    "Sur",
    "Ber",
    "Jah",
    "Cham",
    "Zod",
]

BASES = [
    "Crossbows",
    "Staves",
    "Spears",
    "Scepters",
    "Bows",
    "Axes",
    "Chests",
    "Orbs",
    "Hammers",
    "Staves*",
    "Melee Weapons",
    "Tipped Maces",
    "Wands",
    "Swords",
    "Polearms",
    "Weapons",
    "Melee Weapons ",
    "Claws",
    "Shields",
    "Helms",
    "Scepters ",
    "Clubs",
]


@dataclass
class RuneWord:
    name: str
    bases: List[str]
    runes: List[str]
    level_required: int

    def to_csv(self, runes: List[str]):
        rune_output = []
        for rune in runes:
            if rune in self.runes:
                rune_output.append("1")
            else:
                rune_output.append("0")
        formatted = "\t".join(
            [self.name, str(self.level_required), str(self.bases), str(self.runes), *rune_output]
        )
        return formatted


def process(file_name: str, runewords: Dict[str, RuneWord]):
    with open(f"/Users/Shared/web/portal/tmp/{file_name}", "r") as f:
        soup = BeautifulSoup(f.read(), features="html.parser")

    rw_socket_counts = soup.find_all(string=re.compile("\d-Socket"))

    for i in rw_socket_counts:
        print("-----------------")
        name = i.parent.parent.parent.previous_sibling.previous_sibling.find_all(
            "span"
        )[0].text
        print(name)
        elements = i.parent.parent.parent.find_all("p")
        num_sockets = elements[0].text.split(" ")[0]
        items = " ".join(elements[0].text.split(" ")[1:50]).split("/")
        runes = elements[1].text.split(" • ")
        level = elements[2].text.split(" ")[-1]
        # print(i.parent.parent.parent.find_all("b"))
        runeword = runewords.get(name)
        if runeword:
            runeword.bases.extend(items)
        else:
            runeword = RuneWord(name, items, runes, int(level))
        runewords[name] = runeword
        print(num_sockets)
        print(items)
        print(runes)
        print(level)


def main():
    files = ["rw_chests.html", "rw_helms.html", "rw_weapons.html", "rw_shields.html"]
    runewords: Dict[str, RuneWord] = {}
    for file in files:
        process(file, runewords)
    print(runewords)
    for runeword in runewords.values():
        print(runeword.to_csv(RUNES))

    print("\t".join(RUNES))


if __name__ == "__main__":
    main()
