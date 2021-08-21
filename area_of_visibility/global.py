y, z = 1, 2


def all_global():
    global x
    x = y + z

all_global()
print(x)

