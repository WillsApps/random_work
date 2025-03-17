import re
from os import environ
from pathlib import Path
from re import RegexFlag

from databricks import sql
from databricks.sql.client import Connection

from utils.consts import load_env
from utils.log_utils import logger
from utils.threading import ConnectionWorker, Manager, Worker

load_env()


class DBXWorker(ConnectionWorker):
    def get_connection(self):
        return sql.connect(
            server_hostname=environ.get("DATABRICKS_HOST"),
            http_path=environ.get("DATABRICKS_HTTP_PATH"),
            access_token=environ.get("DATABRICKS_TOKEN"),
        )


def execute_query(connection: Connection, query: str) -> None:
    with connection.cursor() as cursor:
        logger.info(f"Executing query: {query}")
        cursor.execute(query)


def get_queries_from_path(file: Path) -> list[str]:
    raw = file.read_text()
    commentless = re.sub("--.*", "", raw, flags=RegexFlag.MULTILINE)
    return commentless.split(";")


def main(query_file: Path, worker_class=type[Worker]):
    queries = get_queries_from_path(query_file)
    queue = Manager(num_works=10, worker_class=worker_class)
    [
        queue.put((execute_query, {"query": query}))
        for query in queries
        if query.strip() != ""
    ]
    queue.join()


if __name__ == "__main__":
    main(Path("/Users/will.burdett/.scratches/scratch_579.sql"), DBXWorker)
    main(Path("/Users/will.burdett/.scratches/scratch_580.sql"), DBXWorker)
