from threading import Thread, Event
import time


def countdown(n, started_evd):

    print('STARTING')
    started_evd.set()
    while n > 0:
        print(f'NUM {n}')
        n -= 1
        time.sleep(2)


started_evd = Event()
print('Launching countdown')
t = Thread(target=countdown, args=(5, started_evd))
t.start()

started_evd.wait()
print(dir(started_evd))
print('countdown is running')
