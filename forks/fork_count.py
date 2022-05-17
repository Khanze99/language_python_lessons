import os, time


def counter(count):
    for i in range(count):
        time.sleep(1)
        print(f'[{os.getpid()}] => {i}')


if __name__ == '__main__':

    for i in range(5):
        pid = os.fork()

        if pid == 0:
            print(f'Process {os.getpid()} spawned')
        else:
            counter(5)
            os._exit(0)

    print('Main process exiting.')
