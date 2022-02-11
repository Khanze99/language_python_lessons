import time


def tracer(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f'call {calls} to {func.__name__}')
        return func(*args, **kwargs)

    return onCall


def timer(label='', trace=True):

    def onDecorator(func):

        def onCall(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            onCall.alltime += elapsed

            if trace:
                print(f'{label}{func.__name__}: {elapsed:.5f}, {onCall.alltime:.5f}')
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator