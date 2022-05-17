import threading


a = 0
mutex = threading.Lock()


def increment():
    global a
    for i in range(100000):
        mutex.acquire()
        a += 1
        mutex.release()


if __name__ == '__main__':

    t1 = threading.Thread(target=increment, args=())
    t2 = threading.Thread(target=increment, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(a)
