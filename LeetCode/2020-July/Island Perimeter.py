from typing import List
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        def DFS(grid, x, y) -> int:
            grid[x][y] = -1
            num = 4
            # Up
            if x-1 >= 0:
                if grid[x-1][y] == 1:
                    num = num + DFS(grid, x-1, y) - 1
                if grid[x-1][y] == -1:
                    num -= 1
            

            # Right
            if y+1 < len(grid[0]):
                if grid[x][y+1] == 1:
                    num = num  + DFS(grid, x, y+1) - 1
                if grid[x][y+1] == -1:
                    num -= 1
            

            # Down
            if x+1 < len(grid):
                if grid[x+1][y] == 1:
                    num = num + DFS(grid, x+1, y) - 1
                # if grid[x+1][y] == -1:
                #     num -= 1

            # Left
            if y-1 >= 0:
                if grid[x][y-1] == 1:
                    num = num + DFS(grid, x, y-1) - 1
                # if grid[x][y-1] == -1:
                #     num -= 1

            return num


        # res = [[0] * len(grid[0])] * len(grid)
        # res = 0
        res = DFS(grid,0,0)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             res += DFS(grid, i, j)

        return res
    
s1 = Solution()
# print(s1.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(s1.islandPerimeter([[1, 1], [1, 1]]))