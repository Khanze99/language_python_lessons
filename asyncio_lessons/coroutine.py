from types import coroutine
from time import time, sleep
from random import randint


@coroutine
def grep(pattern):
    print("Searching for", pattern)

    while True:
        line = (yield)
        if pattern in line:
            print(line)
            sleep(2)
            yield randint()


if __name__ == '__main__':

    search = grep("coroutine")
    search.__next__()

    search.send("I love you")
    search.send("Don't you love me")
    search.send("I love coroutines instead!")
    search.close()
