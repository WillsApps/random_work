from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Any


class StrEnum(Enum):
    @classmethod
    def from_str(cls, name: str):
        try:
            return cls[name.upper()]
        except KeyError:
            return cls[name.replace(f"{cls.__name__}.", "").upper()]


class DataEnvironment(StrEnum):
    DBX = auto()
    RDS = auto()
    S3 = auto()


EMPTY_ENV_MAP = {env: [] for env in DataEnvironment}


class TestCase(ABC):
    @abstractmethod
    @property
    def dag_conf(self) -> dict[str, Any]:
        raise NotImplementedError()

    @abstractmethod
    @property
    def dag_id(self) -> str:
        raise NotImplementedError()

    @property
    def teardowns_map(self) -> dict[DataEnvironment : list[str]]:
        return EMPTY_ENV_MAP

    @property
    def setups_map(self) -> dict[DataEnvironment : list[str]]:
        return EMPTY_ENV_MAP

    @property
    def assertions_map(self) -> dict[DataEnvironment : list[str]]:
        return EMPTY_ENV_MAP

    def get_teardowns(self, environment: DataEnvironment) -> list[str]:
        return self.teardowns_map.get(environment, [])

    def get_setups(self, environment: DataEnvironment) -> list[str]:
        return self.setups_map.get(environment, [])

    def get_assertions(self, environment: DataEnvironment) -> list[str]:
        return self.assertions_map.get(environment, [])
