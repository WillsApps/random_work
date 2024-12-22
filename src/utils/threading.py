# Stole this code from here
# https://stackoverflow.com/questions/35160417/threading-queue-working-example
from queue import Empty, Queue
from threading import Thread
from typing import List


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


class Manager(Queue):
    def __init__(self, num_works=4):
        super().__init__()
        self.workers: List[Worker] = []
        for _ in range(num_works):
            self.workers.append(Worker(self))
