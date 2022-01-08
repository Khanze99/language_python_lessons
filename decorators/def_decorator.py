

def decorator(C):
    class Wrapped:
        def __init__(self, *args):
            self.wrapped = C(*args)

    return Wrapped


class Wrapper: ...


def decorator(C):
    def onCall(*args):
        return Wrapper(C(*args))
    return onCall
