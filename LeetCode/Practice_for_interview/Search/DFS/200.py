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