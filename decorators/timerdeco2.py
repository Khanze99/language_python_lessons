import time


def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            onCall.alltime += time.time() - start

            if trace:
                print(f'label: {label}, funcname: {func.__name__}, time: {elapsed:.2f}, alltime: {onCall.alltime:.5f}')
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator
