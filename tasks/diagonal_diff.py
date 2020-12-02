a = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]


len_a = len(a) - 1
diagonal_transition = 0
left_sum = 0
right_sum = 0

for i in a:
    left_sum += i[diagonal_transition]
    right_sum += i[len_a]
    diagonal_transition += 1
    len_a -= 1

print(abs(left_sum - right_sum))
