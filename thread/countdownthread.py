from threading import Thread
import time


class CountDownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self) -> None:
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


c = CountDownThread(5)
c.start()
