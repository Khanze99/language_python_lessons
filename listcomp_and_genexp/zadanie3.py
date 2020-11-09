

# List = [ [1, 2, 3], [10, 20,30, 50, 100 ]
# Sum = ?

objs_sum = [[1, 2, 3], [10, 20, 30, 50, 100]]


# в случае, если нам нужно посчитать сумму с каждыми объектами каждой вложенности
sum_all = [a + b for a in objs_sum[0] for b in objs_sum[1]]
print(sum_all)  # -> [11, 21, 31, 51, 101, 12, 22, 32, 52, 102, 13, 23, 33, 53, 103]


# в случае если нам нужно посчитать сумму по позиции объектов
sum_all = list(map(lambda a, b: a + b, objs_sum[0], objs_sum[1]))
print(sum_all)  # -> [11, 22, 33]


# в случае если нам нужно посчитать всю сумму в кажой вложенности
sum_all = sum(objs_sum[0]) + sum(objs_sum[1])
print(sum_all)

# use list comprehension with sum
sum_all = sum([sum(iter) for iter in objs_sum])
print(sum_all)

sum_all = sum([a for nested in objs_sum for a in nested])
print(sum_all)


# use list comprehension use reduce
from functools import reduce
sum_all = reduce(lambda a, b: a +b, [a for nested in objs_sum for a in nested])
print(sum_all)
