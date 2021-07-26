from typing import List

test_data = [
    [2, 2, 1],  # 1
    [4, 1, 2, 1, 2],  # 4
    [1]  # 1
]


class MySolution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:  # o(n^2) ?
                return i
        # time complexity O(n^2)
        # space complexity O(n)


class SolutionO1:
    def singleNumber(self, nums: List[int]) -> int:  # ?
        a = 0
        for i in nums:
            a ^= i
        return a
        # time complexity O(n)
        # space complexity O(1)
