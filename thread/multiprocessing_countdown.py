import time
import multiprocessing


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        print('SET RUNNING FALSE')
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)
