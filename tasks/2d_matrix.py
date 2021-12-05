from typing import List


class Solution:
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        lr, hr = 0, len(matrix) - 1
        row = None

        while lr <= hr:
            row = (lr + hr) // 2

            if matrix[row][0] >= target and matrix[row][len(matrix[row]) - 1] <= target:
                break
            elif matrix[row][0] > target:
                hr = row - 1
            else:
                lr = row + 1

        l, h = 0, len(matrix[row]) - 1

        while l <= h:
            mid = (l + h) // 2
            pick = matrix[row][mid]

            if pick == target:
                return True
            elif target > pick:
                l = mid + 1
            else:
                h = mid - 1
        return False


if __name__ == '__main__':
    matrix, target = [[1], [3]], 1

    Solution.searchMatrix(matrix, target)
