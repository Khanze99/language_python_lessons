from functools import reduce


# Вычисление суммы как всех элементов списка

items = [1, 2, 3, 4, 5]
sum_all = reduce(lambda a, b: a + b, items)
print(sum_all)


# Вычисление наибольшего элемента в списке

items = [1, 8, 66, 21, 99]
obj_max = reduce(lambda a, b: a if (a > b) else b, items)
print(obj_max)
