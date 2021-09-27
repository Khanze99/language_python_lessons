

X = 99


def selector():
    import __main__
    print(__main__.X)
    X = 88
    print(X)


def saver(x=[]):
    x.append(1)
    print(x)

