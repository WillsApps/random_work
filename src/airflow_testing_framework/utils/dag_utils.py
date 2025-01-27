from typing import Any

from airflow.decorators import task


@task()
def get_dag_conf(a: Any):
    return a
