import json
import logging
import os
import time
from queue import Queue, Empty
from threading import Thread
from typing import List

import psycopg2
from dotenv import load_dotenv


VERSION = "v2"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(f"{VERSION}.log"), logging.StreamHandler()],
)
load_dotenv("../../.env")


class Worker(Thread):
    def __init__(self, my_queue: Queue, index: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = get_connection()
        self.index = f"{index}"
        self.created_staging = False
        self.created_map = False

        self.my_queue = my_queue

        self.start()

    def run(self):
        if not self.created_staging:
            create_staging_table(self.conn, self.index)
            self.created_staging = True

        if not self.created_map:
            create_map_table(self.conn, self.index)
            self.created_map = True
        while True:
            try:
                work, kwargs = self.my_queue.get(timeout=3)  # 3s timeout
                work(**kwargs, conn=self.conn, index=self.index)
            except Empty:
                return
            # do whatever work you have to do on work
            self.my_queue.task_done()


class Manager(Queue):
    def __init__(self, num_works=4):
        super().__init__()
        self.workers: List[Worker] = []
        for i in range(num_works):
            self.workers.append(Worker(self, i))


def get_connection():
    conn = psycopg2.connect(
        database=os.environ.get("REDSHIFT_DATABASE"),
        user=os.environ.get("REDSHIFT_USER"),
        password=os.environ.get("REDSHIFT_PASSWORD"),
        host=os.environ.get("REDSHIFT_HOST"),
        port=os.environ.get("REDSHIFT_PORT"),
    )
    return conn


def execute_query(conn, query):
    trans_query = f"""BEGIN;\n{query}\nCOMMIT;"""
    logging.info(f"Running query: \n{trans_query}")
    with conn.cursor() as curs:
        curs.execute(trans_query)
    # conn.commit()


def create_map_table(conn, index: str):
    with open("sql/create_map_table.sql", "r") as f:
        query = f.read()

    execute_query(conn, query.format(version=VERSION, index=index))


def create_staging_table(conn, index: str):
    with open("sql/create_staging_table.sql", "r") as f:
        query = f.read()

    execute_query(conn, query.format(version=VERSION, index=index))


def copy_update(conn, index: str, combo_date: str, file_index: int):
    logging.info(f"Starting query {file_index} of {NUM_FILES}")
    s3_key = f"s3://zola-integration/bliss-point-media/{combo_date}_zola_video_impressions.csv.gz"
    with open("sql/copy_and_insert.sql", "r") as f:
        query = f.read()

    execute_query(
        conn,
        query.format(
            version=VERSION,
            index=index,
            s3_key=s3_key,
            iam_role=os.environ.get("IAM_ROLE"),
        ),
    )


def get_files_to_load():
    with open("rows.json", "r") as f:
        raw = f.read()
    return json.loads(raw)


NUM_FILES = len(get_files_to_load())


def main():
    thread_num = 4
    queue = Manager(thread_num)
    files = get_files_to_load()
    for index, file in enumerate(files):
        queue.put((copy_update, {"combo_date": file, "file_index": index}))

    queue.join()


if __name__ == "__main__":
    main()
