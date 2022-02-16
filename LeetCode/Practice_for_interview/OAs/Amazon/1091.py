'''
https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/solution/bfszui-duan-lu-jing-wen-ti-bfsdfsde-si-k-ngc5/

1.如果只是要找到某一个结果是否存在，那么DFS会更高效。因为DFS会首先把一种可能的情况尝试到底,
才会回溯去尝试下一种情况，只要找到一种情况，就可以返回了。但是BFS必须所有可能的情况同时尝试,
在找到一种满足条件的结果的同时，也尝试了很多不必要的路径

2.如果是要找所有可能结果中最短的，那么BFS回更高效。因为DFS是一种一种的尝试，在把所有可能情况尝试完之前,
无法确定哪个是最短，所以DFS必须把所有情况都找一遍，才能确定最终答案（DFS的优化就是剪枝，不剪枝很容易超时),
而BFS从一开始就是尝试所有情况，所以只要找到第一个达到的那个点，那就是最短的路径，可以直接返回了，其他情况都可以省略了,
所以这种情况下，BFS更高效。


'''



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
                ind, con = que.pop()
                for pos_h, pos_v in [(-1, -1), (-1, 0), (-1, 1), (0 ,1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                    new_ind = ind + pos_h
                    new_con = con + pos_v

                    if 0 <= new_ind < length and 0 <= new_con < length and grid[new_ind][new_con] == 0 and not visited.get((new_ind, new_con)):
                        if new_ind == length - 1 and new_con == length - 1:
                            return start + 1
                        que.appendleft((new_ind, new_con))
                        visited[(new_ind, new_con)] = True
            start += 1

        return -1