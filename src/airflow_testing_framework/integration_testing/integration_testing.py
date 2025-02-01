from dataclasses import dataclass
from datetime import datetime

from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.utils.task_group import TaskGroup
from dataclasses_json import DataClassJsonMixin

from airflow_testing_framework.integration_testing.entities.enums import TestId
from airflow_testing_framework.integration_testing.test_cases.base_test_case import (
    DataEnvironment,
)
from airflow_testing_framework.integration_testing.test_cases.platform_deletes_refinements import (
    PlatformDeletesRefinements,
)
from airflow_testing_framework.utils.dag_utils import get_dag_conf


@dataclass
class DagConf(DataClassJsonMixin):
    test_ids: list[TestId]


TEST_ID_TEST_CASE_MAP = {
    TestId.PLATFORM_DELETES_REFINEMENTS: PlatformDeletesRefinements(),
}


@task
def remove_s3_files(dag_conf: DagConf, items: list[str]) -> None:
    pass


@task
def write_s3_files(dag_conf: DagConf, items: list[str]) -> None:
    pass


@task
def writer_queries_dbx(dag_conf: DagConf, items: list[str]) -> None:
    pass


@task
def writer_queries_rds(dag_conf: DagConf, items: list[str]) -> None:
    pass


@task
def read_s3_files(dag_conf: DagConf, items: list[str]):
    pass


@task
def reader_queries_dbx(dag_conf: DagConf, items: list[str]):
    pass


@task
def reader_queries_rds(dag_conf: DagConf, items: list[str]):
    pass


TEARDOWN_TASK_MAP = {
    DataEnvironment.S3: remove_s3_files,
    DataEnvironment.DBX: writer_queries_dbx,
    DataEnvironment.RDS: writer_queries_rds,
}

SETUP_TASK_MAP = {
    DataEnvironment.S3: write_s3_files,
    DataEnvironment.DBX: writer_queries_dbx,
    DataEnvironment.RDS: writer_queries_rds,
}

ASSERTION_TASK_MAP = {
    DataEnvironment.S3: read_s3_files,
    DataEnvironment.DBX: reader_queries_dbx,
    DataEnvironment.RDS: reader_queries_rds,
}


@task
def get_teardowns(dag_conf: DagConf, environment: DataEnvironment) -> list[str]:
    teardowns = []
    for test_id in dag_conf.test_ids:
        teardowns.extend(TEST_ID_TEST_CASE_MAP[test_id].get_teardowns(environment))
    return teardowns


@task
def get_setups(dag_conf: DagConf, environment: DataEnvironment) -> list[str]:
    setups = []
    for test_id in dag_conf.test_ids:
        setups.extend(TEST_ID_TEST_CASE_MAP[test_id].get_setups(environment))
    return setups


@task
def get_assertions(dag_conf: DagConf, environment: DataEnvironment) -> list[str]:
    assertions = []
    for test_id in dag_conf.test_ids:
        assertions.extend(TEST_ID_TEST_CASE_MAP[test_id].get_assertions(environment))
    return assertions


@task
def run_teardowns(dag_conf: DagConf, environment: DataEnvironment, items: list[str]):
    TEARDOWN_TASK_MAP[environment](dag_conf, items)


@task
def run_setups(dag_conf: DagConf, environment: DataEnvironment, items: list[str]):
    SETUP_TASK_MAP[environment](dag_conf, items)


@task
def run_assertions(dag_conf: DagConf, environment: DataEnvironment, items: list[str]):
    ASSERTION_TASK_MAP[environment](dag_conf, items)


@task
def get_trigger_dag_ids_and_confs(dag_conf: DagConf) -> list[dict[str, str]]:
    return [
        {
            "trigger_dag_id": TEST_ID_TEST_CASE_MAP[test_id].dag_id,
            "conf": TEST_ID_TEST_CASE_MAP[test_id].dag_conf,
        }
        for test_id in dag_conf.test_ids
    ]


default_args = {"owner": "airflow", "params": DagConf(list(TestId)).to_dict()}


@dag(
    default_args=default_args,
    schedule_interval=None,
    start_date=datetime.fromtimestamp(0),
    tags=["example"],
)
def integration_testing():
    start = EmptyOperator(task_id="start")
    dag_conf = get_dag_conf(DagConf(list(TestId)))
    start >> dag_conf

    with TaskGroup("pre_test_teardown") as pre_test_teardown_task_group:
        for env in DataEnvironment:
            teardowns = get_teardowns(dag_conf, env)
            run_teardowns(dag_conf, env, teardowns)

    with TaskGroup("setups") as setups_task_group:
        for env in DataEnvironment:
            setups = get_setups(dag_conf, env)
            run_setups(dag_conf, env, setups)
    pre_test_teardown_task_group >> setups_task_group

    with TaskGroup("trigger_dags") as trigger_dags_task_group:
        trigger_dag_ids_and_confs = get_trigger_dag_ids_and_confs(dag_conf)

        TriggerDagRunOperator.partial(task_id="trigger_dags").expand_kwargs(
            trigger_dag_ids_and_confs
        )
    setups_task_group >> trigger_dags_task_group

    with TaskGroup("assertions") as assertions_task_group:
        for env in DataEnvironment:
            assertions = get_assertions(dag_conf, env)
            run_assertions(dag_conf, env, assertions)
    trigger_dags_task_group >> assertions_task_group
