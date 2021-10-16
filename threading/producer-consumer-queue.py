import random
import logging
import concurrent.futures as future
import threading
import time
import queue


SENTINEL = object()


def producer(pipeline, event):
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info(f"Producer got message: {message}")
        pipeline.set_message(message, "Produser")

    logging.info("Producer received EXIT event. Exiting")


def consumer(pipeline, event):
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            f"Consumer storing message: {message} (queue size={pipeline.qsize()})"
        )

    logging.info("Consumer received EXIT event. Exiting")


class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug(f"{name}:about to get from queue")
        value = self.get()
        logging.debug(f"{name}:got {value} from queue")
        return value

    def set_message(self, value, name):
        logging.debug(f"{name}: about to add {value} to queue")
        self.put(value)
        logging.debug(f"{name}:added {value} to queue")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    pipline = Pipeline()
    event = threading.Event()
    logging.getLogger().setLevel(logging.DEBUG)

    with future.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipline, event)
        executor.submit(consumer, pipline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
