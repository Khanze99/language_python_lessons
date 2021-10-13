import random
import logging
import concurrent.futures as future
import threading
import time


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


class Pipeline:
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        # logging.debug(f"{name}:about to acquire getlock")
        self.consumer_lock.acquire()
        # logging.debug(f"{name}:have getlock")
        message = self.message
        # logging.debug(f"{name}:about to release setlock")
        self.producer_lock.release()
        # logging.debug(f"{name}:setlock released")
        return message

    def set_message(self, message, name):
        # logging.debug(f"{name}: about to acquire setlock")
        self.producer_lock.acquire()
        # logging.debug(f"{name}:have setlock")
        self.message = message
        # logging.debug(f"{name}:about to release getlock")
        self.consumer_lock.release()
        # logging.debug(f"{name}:getlock released")


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