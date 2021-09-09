import sys



def intersect(*args):
    print(args[0], args[1:])
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break

        else:
            res.append(x)

    return res


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)

    return res


def print3(*args, **kwargs):
    sep = kwargs.pop('sep', ' ')
    end = kwargs.pop('end', '\n')
    file = kwargs.pop('file', sys.stdout)

    if kwargs: raise TypeError('extra keywords: %s' % kwargs)
    output = ''
    first = True

    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False

    file.write(output + end)
