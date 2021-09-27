
def adder(*args):
    s = args[0]
    for n in args[1:]:
        s += n
    return s
