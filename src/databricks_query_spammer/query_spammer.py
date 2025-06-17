import re
from datetime import datetime, timedelta
from math import floor
from os import environ
from pathlib import Path
from re import RegexFlag

from databricks import sql
from databricks.sql.client import Connection
from general_utils.consts import load_env
from general_utils.log_utils import logger
from general_utils.threading import ConnectionWorker, Manager, Worker

load_env()


class DBXWorker(ConnectionWorker):
    def get_connection(self):
        return sql.connect(
            server_hostname=environ.get("DATABRICKS_HOST"),
            http_path=environ.get("DATABRICKS_HTTP_PATH"),
            access_token=environ.get("DATABRICKS_TOKEN"),
        )


def get_expected_end_time(
    start_time: datetime,
    index: int,
    total: int,
) -> tuple[timedelta, datetime]:
    if index == 0:
        time_left = timedelta(hours=1000)
        return time_left, datetime.now() + time_left
    now = datetime.now()
    percent_finished = float(index) / total
    duration = now - start_time
    time_left = duration / percent_finished - duration
    end_time = now + time_left
    return time_left, end_time


def pretty_timedelta(delta: timedelta) -> str:
    parts = []
    if delta.days:
        parts.append(f"days={delta.days}")
    seconds = delta.seconds
    if seconds >= 3600:
        hours = floor(seconds / 3600)
        seconds = seconds - hours * 3600
        parts.append(f"hours={hours}")
    if seconds >= 60:
        minutes = floor(seconds / 60)
        seconds = seconds - minutes * 60
        parts.append(f"minutes={minutes}")
    parts.append(f"seconds={seconds}")
    return f'({", ".join(parts)})'


def execute_query(
    connection: Connection,
    query: str,
    index: int,
    total: int,
    start_time: datetime,
) -> None:
    time_left, expected_end_time = get_expected_end_time(start_time, index, total)
    with connection.cursor() as cursor:
        logger.info(
            f"Task: ({index}/{total}) time_left: ({pretty_timedelta(time_left)}), expected_end_time:({expected_end_time.isoformat()}):\n{query.strip()}"
        )
        try:
            cursor.execute(query)
        except Exception:
            logger.exception(f"Failed for task: ({index}/{total})")
            raise


def get_queries_from_path(file: Path) -> list[str]:
    raw = file.read_text()
    commentless = re.sub("--.*", "", raw, flags=RegexFlag.MULTILINE)
    return commentless.split(";")


def main(query_file: Path, worker_class=type[Worker]):
    start_time = datetime.now()
    queries = get_queries_from_path(query_file)
    queue = Manager(num_works=10, worker_class=worker_class)
    [
        queue.put(
            (
                execute_query,
                {
                    "query": query,
                    "start_time": start_time,
                    "index": index,
                    "total": len(queries),
                },
            )
        )
        for index, query in enumerate(queries)
        if query.strip() != ""
    ]
    queue.join()


if __name__ == "__main__":
    main(Path("/Users/will.burdett/.scratches/scratch_579.sql"), DBXWorker)
    main(Path("/Users/will.burdett/.scratches/scratch_580.sql"), DBXWorker)
    # main(Path("/Users/will.burdett/.scratches/scratch_666.sql"), DBXWorker)
