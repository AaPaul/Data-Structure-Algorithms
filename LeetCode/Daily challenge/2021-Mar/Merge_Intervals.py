from typing import List

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp = intervals[0]
        res = []
        for i in intervals:
            if temp[1] >= i[0] or temp[0] >= i[0]:
                temp = [min(temp[0], i[0]), max(temp[1], i[1])]
            else:
                res.append(temp)
                temp = i
        res.append(temp)
        return res
