

n = 10
nums = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]


def count_height(n, nums):
    for i in enumerate(nums):
        if nums[i] == -1:
            count_height(nums[i], nums)

        print(i)


count_height(n, nums[:])
