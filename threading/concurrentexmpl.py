import logging
import concurrent.futures
import time
import random


def threading_func(name):
    logging.info("Thread %s: starting", name)
    seconds = random.randint(2, 10)
    logging.info("seconds thread %s" % seconds)
    time.sleep(seconds)
    logging.info("Thread %s: finishing", name)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(threading_func, range(3))
