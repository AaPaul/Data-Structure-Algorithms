from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x:x[1])
        ans = 1
        prev = points[0][1]
        for i in range(1, len(points)):
            if prev < points[i][0]:
                ans += 1
                prev = points[i][1]
        
        return ans