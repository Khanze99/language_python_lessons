import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting" % name)
    time.sleep(2)
    logging.info("Thread %s: finishing" % name)


if __name__ == '__main__':
    frmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=frmt, level=logging.INFO, datefmt="%H:%M:S")
    threads = list()

    for index in range(3):

        logging.info("Main               : create and start thread %d", index)
        x = threading.Thread(target=thread_function, args=(index,), daemon=True)
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main               : before joining thread %d", index)
        thread.join()
        logging.info("Main               : thread %d done", index)
    # logging.info("Main    : Before creating thread")
    # x = threading.Thread(target=thread_function, args=(1, ), daemon=True)
    # logging.info("Main    : Before running thread")
    # x.start()
    # logging.info("Main    : wait for the thread to finish")
    # x.join()
    # logging.info("Main    : all done")
