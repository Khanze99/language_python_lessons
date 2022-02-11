class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        print(target, nums)
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2

            if target == nums[mid]: return True

            if nums[low] < nums[mid]:
                if nums[mid] > target > nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target:
                    low = mid
                else:
                    high = mid
        return False


if __name__ == '__main__':
    tests = [
        # {'target': 6, 'nums': [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]},
        # {'target': 4, 'nums': [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]},
        # {'target': 2, 'nums': [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]},
        {'target': 0, 'nums': [1, 0, 1, 1, 1]},
    ]

    for test in tests:
        assert Solution().search(**test)
