from airflow.decorators import task
from beartype.typing import Any


@task()
def get_dag_conf(a: Any):
    return a
