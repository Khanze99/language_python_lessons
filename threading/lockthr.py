import threading
import logging
import time
from concurrent.futures import ThreadPoolExecutor


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info(f"Thread {name}: starting update")
        logging.debug(f"Thread {name}: about to lock")

        with self._lock:
            logging.debug(f"Thread {name}: has lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(2)
            self.value = local_copy
            logging.debug(f"Thread {name}: about to release lock")

        logging.debug(f"Thread {name}: after release")
        logging.debug(f"Thread {name}: finishing update")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d", database.value)
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d", database.value)

