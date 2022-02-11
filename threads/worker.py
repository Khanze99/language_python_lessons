from threading import Semaphore, Thread


def worker(n, sema):
    sema.acquire()
    print('Working', n)


sema = Semaphore(0)
nworkers = 10


for n in range(nworkers):
    t = Thread(target=worker, args=(n, sema))
    t.start()

sema.release()
sema.release()
sema.release()
sema.release()
sema.release()