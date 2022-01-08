import sys
from timerdeco2 import timer

force = list if sys.version_info[0] == 3 else (lambda x: x)


@timer(label='[CCC]==>')
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


for func in (listcomp, mapcall):
    res = func(5)

    func(500000)
    func(5000000)
    func(10000000)

    print(res)

    print(f'allTime = {func.alltime}')
print(f'**map/comp = {round(mapcall.alltime/listcomp.alltime, 3)}')