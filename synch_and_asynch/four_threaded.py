import time
import threading


COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


t1 = threading.Thread(target=countdown, args=(COUNT//4,))
t2 = threading.Thread(target=countdown, args=(COUNT//4,))
t3 = threading.Thread(target=countdown, args=(COUNT//4,))
t4 = threading.Thread(target=countdown, args=(COUNT//4,))

start = time.time()
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
end = time.time()

print('Затраченное время - ', end - start)