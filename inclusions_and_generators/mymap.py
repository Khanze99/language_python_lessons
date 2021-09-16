

def mymap1(func, *seq):
    res = []
    print(list(zip(*seq)))
    for args in zip(*seq):
        print(*args)
        res.append(func(*args))
    return res


def mymap2(func, *seq):
    return [func(*args) for args in zip(*seq)]


def mymap_gen3(func, *seq):
    for args in zip(*seq):
        yield func(*args)


def mymap(func, *seq):
    return (func(*args) for args in zip(*seq))
