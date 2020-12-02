# найти числа, в паре которых сумма равна нулю

nums = [1, 2, 3, 4, -3, -2, -1, -5, -6, 0, 6, 0, 0]

result = []
count = len(list(filter(lambda x: x == 0, nums)))


def arifm_prog(count):
    return int(count * (count - 1) / 2)


for n in filter(lambda x: x > 0, nums):
    if -n in nums:
        result.append([n, -n])


for i in range(arifm_prog(count)):
    result.append([0, 0])

print(result)
