import manynames

X = 66
print(X)
print(manynames.X)  # атрибут модуля
manynames.f()  # 11
manynames.g()

print(manynames.C.X)
I = manynames.C()
print(I.X)
I.m()
print(I.X)
