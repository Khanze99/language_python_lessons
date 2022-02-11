import threading
import time


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:  # как выходит отсюда? демон сразу завершает работу, как завершит программа или процесс
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                print('change flag and wait Condition')
                self._cv.wait()


ptimer = PeriodicTimer(5)
ptimer.start()


def countdowm(nticks):
    while nticks > 0:
        print(f'wait in {countdowm.__name__}')
        ptimer.wait_for_tick()
        print('minus', nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        print(f'wait in {countup.__name__}')
        ptimer.wait_for_tick()
        print('counting', n)
        n += 1


threading.Thread(target=countdowm, args=(10, )).start()
threading.Thread(target=countup, args=(5, )).start()


