from typing import Any

from airflow_testing_framework.entities.constants import SILVER_CATALOG
from airflow_testing_framework.integration_testing.test_cases.base_test_case import (
    DataEnvironment,
    TestCase,
)


class PlatformDeletesRefinements(TestCase):
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
    def teardowns_map(self) -> dict[DataEnvironment : list[str]]:
        return {
            DataEnvironment.DBX: [
                f"DELETE FROM {SILVER_CATALOG}.platform.deletes WHERE refresh_version = '{self.refresh_version}';",
            ]
        }

    @property
    def setups_map(self) -> dict[DataEnvironment : list[str]]:
        return {
            DataEnvironment.DBX: [
                f"INSERT INTO {SILVER_CATALOG}.platform.deletes (refresh_version) VALUES ('{self.refresh_version}');)",
            ]
        }

    @property
    def assertions_map(self) -> dict[DataEnvironment : list[str]]:
        return {
            DataEnvironment.DBX: [
                f"SELECT count(*) = 1 AS is_passing FROM {SILVER_CATALOG}.platform.deletes WHERE refresh_version = '{self.refresh_version}';)",
            ]
        }
