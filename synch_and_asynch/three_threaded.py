import time
import threading


COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


t1 = threading.Thread(target=countdown, args=(COUNT//3,))
t2 = threading.Thread(target=countdown, args=(COUNT//3,))
t3 = threading.Thread(target=countdown, args=(COUNT//3,))

start = time.time()
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end = time.time()

print('Затраченное время - ', end - start)