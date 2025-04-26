import json
import random
from collections import OrderedDict
from collections.abc import Iterable
from typing import Any, TypeVar

BASE_DURATION = 20.0


def get_duration_mod(faster_mods: Iterable[float]) -> float:
    return 100.0 / (sum(faster_mods) + 100.0)


def get_duration(
    faster_mods: list[float], base_duration: float = BASE_DURATION
) -> float:
    return base_duration * get_duration_mod(faster_mods)


def get_highest_stack(faster_mods: list[float]) -> list[int]:
    highest_stacks = []
    debuff_duration = get_duration(faster_mods)
    print(f"{faster_mods=}")
    print(f"    {debuff_duration=}")
    for _ in range(50):
        stacks = {
            0: {"duration_remaining": -1.0, "current_stack": 0, "highest_stack": 0},
            1: {"duration_remaining": -1.0, "current_stack": 0, "highest_stack": 0},
            2: {"duration_remaining": -1.0, "current_stack": 0, "highest_stack": 0},
            3: {"duration_remaining": -1.0, "current_stack": 0, "highest_stack": 0},
        }
        for _ in range(10_000):
            debuff_picked = random.randint(0, 3)
            for mod_id in stacks.keys():
                if mod_id == debuff_picked:
                    stacks[mod_id]["duration_remaining"] = debuff_duration
                    stacks[mod_id]["current_stack"] += 1
                    stacks[mod_id]["highest_stack"] = max(
                        stacks[mod_id]["highest_stack"], stacks[mod_id]["current_stack"]
                    )
                else:
                    stacks[mod_id]["duration_remaining"] -= 1
                    if stacks[mod_id]["duration_remaining"] <= 0:
                        stacks[mod_id]["current_stack"] = 0
        highest_stack = 0
        for mod_id in stacks.keys():
            highest_stack = max(highest_stack, stacks[mod_id]["highest_stack"])
        highest_stacks.append(highest_stack)
    print(f"    {highest_stacks=}")
    print(f"    {sum(highest_stacks)/len(highest_stacks)=}")
    return highest_stacks


def main():
    faster_mods = [
        100.0,
        100.0,
        50.0,
        15.0,
        15.0,
        20.0,
        20.0,
    ]
    for i in range(1, len(faster_mods) + 1):
        print(json.dumps(get_highest_stack(faster_mods[0:i]), indent=2))


DictKeyT = TypeVar("DictKeyT")


def get_key_at_index(faster_mods: OrderedDict[DictKeyT, Any], index: int) -> DictKeyT:
    if index >= len(faster_mods) or index < -1:
        raise IndexError("index out of range")
    if index == -1:
        index = len(faster_mods) - 1
    for place, key in enumerate(faster_mods.keys()):
        if place == index:
            return key


def get_mods_from_index(
    faster_mods: OrderedDict[float, int], i: int
) -> OrderedDict[float, int]:
    mods = OrderedDict()
    for place, faster in enumerate(faster_mods.keys()):
        if place >= i:
            break
        mods[faster] = faster_mods[faster]
    return mods


if __name__ == "__main__":
    main()
