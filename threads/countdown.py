import time
from threading import Thread


def request(n):
    while n > 0:
        print(f'GET REQUEST - {n}')
        n -= 1
        time.sleep(3)


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


t = Thread(target=countdown, args=(10, ))
t.start()

t2 = Thread(target=request, args=(5,))
t2.start()

# t.join()
print('HELLO')
#
while True:
    if t.is_alive():
        print('-' * 20 + 'COUNTDOWN ALIVE' + '-' * 20)
    if t2.is_alive():
        print('-' * 20 + 'REQUEST ALIVE' + '-' * 20)

    if not t.is_alive() and not t2.is_alive():
        print('COMPLETED')
        break
    time.sleep(5)
