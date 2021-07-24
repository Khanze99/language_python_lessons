from typing import List

intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]  # [[1, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]  # [[1, 5]]


class Solution:  # time complexity O(n log n) space complexity O(log N) or O(n)
    def merge(self, intervals: List[List[int]]):
        intervals = sorted(intervals, key=lambda l: l[0])
        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
                continue

            if interval[0] <= res[-1][-1]:
                min_interval = min(res[-1], interval, key=lambda l: l[0])[0]
                max_interval = max(res[-1], interval, key=lambda l: l[-1])[-1]
                res[-1][-1] = max_interval
                res[-1][0] = min_interval
            else:
                res.append(interval)

        return res
