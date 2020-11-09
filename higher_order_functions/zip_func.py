a = [1, 2, 3]
b = "xyz"
c = (None, True)

res = list(zip(a, b, c))
print(res)

res = dict(zip(a, b))
print(res)
