from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low > high:
            mid = (high + low) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] > target > nums[low]:
                high = mid - 1
            elif nums[mid] < target < nums[high]:
                low = mid + 1
            elif nums[high] > target < nums[mid]:
                low = mid
            elif nums[low] > target < nums[mid]:
                high = mid
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3

    print(Solution().search(nums, target))