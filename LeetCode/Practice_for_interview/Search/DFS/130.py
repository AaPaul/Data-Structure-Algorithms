class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(x, y):
            if (x < 0 or x >= m or y < 0 or y >=n or board[x][y] != 'O'):
                return
            board[x][y] = 'T'
            for xi, yi in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dfs(x+xi, y+yi)
                
        m, n = len(board), len(board[0])

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'