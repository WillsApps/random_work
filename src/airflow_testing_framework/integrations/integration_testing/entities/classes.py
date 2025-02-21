from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Optional

from dataclasses_json import DataClassJsonMixin
from entities.constants import REFRESH_VERSION
from integrations.integration_testing.entities.enums import DataEnvironment


@dataclass
class DagConf(DataClassJsonMixin):
    refresh_version: str = f"R{REFRESH_VERSION}"


@dataclass
class IntTestAction(DataClassJsonMixin):
    """
    A class to represent an action to be performed in the DataEnvironment.

    TestActions that share a group_by_key are not run in parallel to avoid table locks or similar.
    """

    env: DataEnvironment
    action: str
    group_by_key: Optional[str] = None


class IntTestCase(ABC):
    _teardowns_map: dict[DataEnvironment, list[IntTestAction]]
    _setups_map: dict[DataEnvironment, list[IntTestAction]]
    _assertions_map: dict[DataEnvironment, list[IntTestAction]]

    @abstractmethod
    @property
    def dag_conf(self) -> dict[str, Any]:
        raise NotImplementedError()

    @abstractmethod
    @property
    def dag_id(self) -> str:
        raise NotImplementedError()

    @property
    def teardowns(self) -> list[IntTestAction]:
        return []

    @property
    def setups(self) -> list[IntTestAction]:
        return []

    @property
    def assertions(self) -> list[IntTestAction]:
        return []

    def get_teardowns(self, environment: DataEnvironment) -> list[IntTestAction]:
        if not self._teardowns_map:
            self._teardowns_map = fill_actions_map(self.teardowns)
        return self._teardowns_map.get(environment, [])

    def get_setups(self, environment: DataEnvironment) -> list[IntTestAction]:
        if not self._setups_map:
            self._setups_map = fill_actions_map(self.setups)
        return self._setups_map.get(environment, [])

    def get_assertions(self, environment: DataEnvironment) -> list[IntTestAction]:
        if not self._assertions_map:
            self._assertions_map = fill_actions_map(self.assertions)
        return self._assertions_map.get(environment, [])


def fill_actions_map(
    actions: list[IntTestAction],
) -> dict[DataEnvironment, list[IntTestAction]]:
    actions_map: dict[DataEnvironment, list[IntTestAction]] = defaultdict(list)
    for action in actions:
        actions_map[action.env].append(action)
    return actions_map
