

a = 1
b = a
b = 2

print(a, b)


x = [1, 2, 3]
l = x
l[0] = 500

print(x, l)


def f(a, b):
    a = 99
    b[0] = 'spam'


X = 100
L = [1, 2, 3]

f(X, L)
print(X, L)
