from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        l = len(nums) - 1
        pointer = 0
        index = 0

        while index < l:
            pointer += 1

            n = target - nums[pointer]
            if h.get(n, None):
                return [h[n], pointer]
            else:
                h[nums[index]] = index

            if pointer == l:
                index += 1
                pointer = index

        return []


if __name__ == '__main__':
    tests = [
        {'nums': [2, 7, 11, 15], 'target': 9},
        {'nums': [2, 7, 11, 15], 'target': 26},
        {'nums': [2, 7, 11, 15], 'target': 18},
        {'nums': [3, 2, 3], 'target': 6}
    ]
    solution = Solution()

    for test in tests:
        print(solution.twoSum(**test))
