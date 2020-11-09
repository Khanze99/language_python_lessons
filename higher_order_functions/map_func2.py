
# 1
l1 = [1, 2, 3]
l2 = [4, 5, 6]

new_list = list(map(lambda x, y: x + y, l1, l2))
print(new_list)


# 2 Если же количество элементов в списках совпажать не будет, то выполнение закончится на минимальном списке:

l1 = [1, 2, 3]
l2 = [4, 5]

new_list = list(map(lambda x, y: x + y, l1, l2))
print(new_list)