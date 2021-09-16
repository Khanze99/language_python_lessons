

def sumtree_rec(L):
    tot = 0
    for x in L:
        print(x)
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree_rec(x)
    return tot


def sumtree_stack(L):
    tot = 0
    items = list(L)

    while items:
        front = items.pop(0)
        print(front)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)

    return tot


def sumtree(L):
    tot = 0
    items = list(L)

    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
            print(items)

    return tot
