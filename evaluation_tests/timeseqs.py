import sys
import timer

reps = 10000
repslist = list(range(reps))


def f(x): return x


def for_loop():
    res = []
    for x in repslist:
        res.append(f(x))

    return res


def list_comp():
    return [f(x) for x in repslist]


def map_call():
    return list(map(f, repslist))


def gen_expr():
    return list(f(x) for x in repslist)


def gen_func():
    def gen():
        for x in repslist:
            yield f(x)

    return list(gen())


print(sys.version)

for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print(
        '%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1])
    )
