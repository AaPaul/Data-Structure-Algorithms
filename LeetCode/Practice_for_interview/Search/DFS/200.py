class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return 0
            area = 1
            grid[x][y] = '0'
            
            for xi, yi in directions:
                area += dfs(x+xi, y+yi)
            
            return area
        
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        islands = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    t = dfs(i, j)
                    islands += 1
        return islands



from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited m x n
        # T: O(mn), S: O(mn)
        def dfs(x, y):
            if grid[x][y] == '0' or visited[x][y]:
                return
            visited[x][y] = 1
            
            for xi, yi in ([-1,0],[1,0],[0, -1], [0, 1]):
                if 0 <= x + xi < m and 0 <= y + yi < n:
                    dfs(x + xi, y + yi)
    
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        # print(visited)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    res += 1
        return res

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s1 = Solution()
print(s1.numIslands(grid))