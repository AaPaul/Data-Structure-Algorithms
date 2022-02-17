class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        plated = 0
        left, right = newInterval
        res = []
        for li, ri in intervals:
            if li > right:
                if plated == 0:
                    res.append([left, right])
                    plated = 1
                res.append([li, ri])
            elif ri < left:
                res.append([li, ri])
            else:
                left = min(li, left)
                right = max(ri, right)
        if plated == 0:
            res.append([left, right])
        return res