from typing import Any

from entities.constants import SILVER_CATALOG
from integrations.integration_testing.entities.classes import IntTestAction, IntTestCase
from integrations.integration_testing.entities.enums import DataEnvironment


class PlatformDeletesRefinements(IntTestCase):
    refresh_version = "R00"

    @property
    def dag_id(self) -> str:
        return "platform_deletes"

    @property
    def dag_conf(self) -> dict[str, Any]:
        return {
            "refresh_version": self.refresh_version,
        }

    @property
    def teardowns(self) -> list[IntTestAction]:
        return [
            IntTestAction(
                DataEnvironment.DBX,
                f"DELETE FROM {SILVER_CATALOG}.platform.deletes WHERE refresh_version = '{self.refresh_version}';",
                f"{SILVER_CATALOG}.platform.deletes",
            )
        ]

    @property
    def setups(self) -> list[IntTestAction]:
        return [
            IntTestAction(
                DataEnvironment.DBX,
                f"INSERT INTO {SILVER_CATALOG}.platform.deletes (refresh_version) VALUES ('{self.refresh_version}');)",
            ),
        ]

    @property
    def assertions(self) -> list[IntTestAction]:
        return [
            IntTestAction(
                DataEnvironment.DBX,
                f"SELECT count(*) = 1 AS is_passing FROM {SILVER_CATALOG}.platform.deletes WHERE refresh_version = '{self.refresh_version}';)",
            ),
        ]
