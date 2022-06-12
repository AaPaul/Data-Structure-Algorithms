class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            ans = 1
            grid[x][y] = 0
            for xi, yi in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ans += dfs(x+xi, y+yi)
            return ans
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                max_area = max(max_area, dfs(i, j))
        
        return max_area