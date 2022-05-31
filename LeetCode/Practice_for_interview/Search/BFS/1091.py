from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        length = len(grid)
        if length == 1:
            return 1
        que = deque()
        visited = {}
        que.appendleft((0,0))
        visited[(0, 0)] = True
        start = 1
        while que:
            for _ in range(len(que)):
                idx, col = que.pop()
                for pos_x, pos_y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (-1, 0), (1, 1)]:
                    new_idx, new_col = idx + pos_x, col + pos_y
                    if 0 <= new_idx < length and 0 <= new_col < length and grid[new_idx][new_col] == 0 and not visited.get((new_idx, new_col)):
                        if new_idx == length - 1 and new_col == length - 1:
                            return start + 1
                        
                        que.appendleft((new_idx, new_col))
                        visited[(new_idx, new_col)] = True
                
            start += 1
        return -1