import logging
import sys
import time
from collections.abc import Callable
from typing import TypeVar


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


logger = get_logger(__name__)

T = TypeVar("T")


def timeit(func: Callable[..., T]) -> T:
    def wrapper(*args, **kwargs) -> T:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug(f"Finished in {end - start} seconds")
        return result

    return wrapper
