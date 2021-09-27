

def gen(x):
    while True:
        yield x
        print(x)
        x -= 1
        if x < 0:
            raise StopIteration

