

def get_tuple_n(n):
    return n, n**2, n**3


range_n = range(1, 10)  # range(1, n)

n_list = list(map(get_tuple_n, range_n))
print(n_list)


n_list = list(map(lambda n: (n, n**2, n**3), range_n))  # решение
print(n_list)
