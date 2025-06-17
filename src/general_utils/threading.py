# Stole this code from here
# https://stackoverflow.com/questions/35160417/threading-queue-working-example
from abc import ABC, abstractmethod
from queue import Empty, Queue
from threading import Thread

from general_utils.log_utils import logger


class Worker(Thread):
    def __init__(self, my_queue: Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_queue = my_queue
        self.start()

    def run(self):
        while True:
            try:
                work, kwargs = self.my_queue.get(timeout=3)  # 3s timeout
                work(**kwargs)
            except Empty:
                return
            # do whatever work you have to do on work
            self.my_queue.task_done()


class ConnectionWorker(Worker, ABC):
    def __init__(self, *args, **kwargs):
        self.connection = self.get_connection()
        super().__init__(*args, **kwargs)

    @abstractmethod
    def get_connection(self):
        raise NotImplementedError

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
                break
            # do whatever work you have to do on work
            self.my_queue.task_done()


class Manager(Queue):
    def __init__(self, num_works=4, worker_class=type[Worker]):
        super().__init__()
        self.workers: list[worker_class] = []
        for _ in range(num_works):
            self.workers.append(worker_class(self))
