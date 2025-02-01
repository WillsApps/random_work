from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

from airflow_testing_framework.entities.constants import REFRESH_VERSION


@dataclass
class DagConf(DataClassJsonMixin):
    refresh_version: str = f"R{REFRESH_VERSION}"
