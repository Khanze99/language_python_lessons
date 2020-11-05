import functools

from clockdeco2 import clock


@functools.lru_cache()  # принимает конфигурационные параметры maxsize и typed
@clock
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(6))
