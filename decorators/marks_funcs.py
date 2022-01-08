

def decorate(func):
    func.marked = True

    return func


@decorate
def spam(a, b):
    return a + b

