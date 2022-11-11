import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x:[x[0], -x[1]])
        rooms = [intervals[0][1]]
        for i in range(1, n):
            if rooms[0] > intervals[i][0]:
                heapq.heappush(rooms, intervals[i][1])
            else:
                heapq.heappushpop(rooms, intervals[i][1])
        return len(rooms)

intervals = [[0,31],[5,11],[15,21]]
intervals = [[4, 9], [9, 16], [4, 16]]

s1 = Solution()
print(s1.minMeetingRooms(intervals))