# The DFS works well with Java while in python version I don't know why there always some problems

from typing import List
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        def DFS(grid, x:int, y:int) -> int:
            # grid[x][y] = -1
            visted[x][y] = 1
            num = 4
            # Up
            if x-1 >= 0:
                if grid[x-1][y] == 1 and not visted[x-1][y]:
                    num = num + DFS(grid, x-1, y) - 1
                # if grid[x-1][y] == -1:
                elif visted[x-1][y]:
                    num -= 1
            

            # Right
            if y+1 < len(grid[0]):
                if grid[x][y+1] == 1 and not visted[x][y-1]:
                    num = num  + DFS(grid, x, y+1) - 1
                # if grid[x][y+1] == -1:
                elif visted[x][y+1]:
                    num -= 1
            

            # Down
            if x+1 < len(grid):
                if grid[x+1][y] == 1 and not visted[x+1][y]:
                    num = num + DFS(grid, x+1, y) - 1
                # if grid[x+1][y] == -1:
                elif visted[x+1][y]:
                    num -= 1

            # Left
            if y-1 >= 0:
                if grid[x][y-1] == 1 and not visted[x][y-1]:
                    num = num + DFS(grid, x, y-1) - 1
                # if grid[x][y-1] == -1:
                elif visted[x][y-1]:
                    num -= 1

            return num


        # res = [[0] * len(grid[0])] * len(grid)
        #  不能用这种创建列表，这是一种浅复制，当你给res[1][0]赋值时，res[2][0],res[3][0]会同时改变. 因为第二，三行都是对第一行的一个浅复制
        res = 0
        visted = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        # res = DFS(grid,0,0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visted[i][j]:
                    res += DFS(grid, i, j)

        return res
    
s1 = Solution()
print(s1.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(s1.islandPerimeter([[1, 1], [1, 1]]))
print(s1.islandPerimeter([[1, 1, 0]]))
print(s1.islandPerimeter([[1, 0], [1, 0], [1, 0]]))

# https://blog.csdn.net/nxhyd/article/details/72325783
# https://blog.csdn.net/zxzxzx0119/article/details/82966388