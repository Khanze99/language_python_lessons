from queue import Queue
from threading import Thread


_sentinel = object()


def producer(out_q):
    data = 0
    while data < 10:
        print('PUT DATA: ', data)
        out_q.put(data)
        data += 1
    out_q.put(_sentinel)


def consumer(in_q):
    while True:
        data = in_q.get()
        print('GET FROM QUEUE: ', data)
        if data is _sentinel:
            break


q = Queue()

t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))

t1.start()
t2.start()
