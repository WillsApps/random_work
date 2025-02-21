import re
from os import environ
from pathlib import Path
from queue import Empty
from re import RegexFlag

from databricks import sql
from databricks.sql.client import Connection

from databricks_query_spammer import logger
from utils.consts import load_env
from utils.threading import Manager, Worker

load_env()


class ConnectionWorker(Worker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection = sql.connect(
            server_hostname=environ.get("DATABRICKS_HOST"),
            http_path=environ.get("DATABRICKS_HTTP_PATH"),
            access_token=environ.get("DATABRICKS_TOKEN"),
        )

    def run(self):
        while True:
            try:
                work, kwargs = self.my_queue.get(timeout=3)  # 3s timeout
                work(connection=self.connection, **kwargs)
            except Empty:
                self.connection.close()
                logger.info("Closing connection.")
                return
            except Exception as ex:
                self.connection.close()
                logger.exception(ex)
                logger.exception("Closing connection.")
            # do whatever work you have to do on work
            self.my_queue.task_done()


def execute_query(connection: Connection, query: str) -> None:
    with connection.cursor() as cursor:
        logger.info(f"Executing query: {query}")
        cursor.execute(query)


def get_queries_from_path(file: Path) -> list[str]:
    raw = file.read_text()
    commentless = re.sub("--.*", "", raw, flags=RegexFlag.MULTILINE)
    return commentless.split(";")


def main(query_file: Path):
    queries = get_queries_from_path(query_file)
    queue = Manager(num_works=10, worker_class=ConnectionWorker)
    [
        queue.put((execute_query, {"query": query}))
        for query in queries
        if query.strip() != ""
    ]
    queue.join()


if __name__ == "__main__":
    main(Path("/Users/will.burdett/.scratches/scratch_579.sql"))
    main(Path("/Users/will.burdett/.scratches/scratch_580.sql"))
