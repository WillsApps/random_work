from collections.abc import Sized

from beartype.typing import TypeVar

BatchReturnT = TypeVar("BatchReturnT")


def batch(iterable: Sized[BatchReturnT], size: int = 1) -> Sized[Sized[BatchReturnT]]:
    return [iterable[i : i + size] for i in range(0, len(iterable), size)]
