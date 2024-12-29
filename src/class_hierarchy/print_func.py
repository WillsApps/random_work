from typing import Callable

from src.class_hierarchy.classes import CLASS_MAP


def print_all(works: list[str], func: Callable):
    for index, work in enumerate(works):
        class_func = CLASS_MAP[work].__getattribute__(func.__name__)
        class_func(index)
