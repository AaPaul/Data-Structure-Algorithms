class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def DFS(b1, i, j):
            if b1[i][j] == 'O':
                b1[i][j] = 'N'
                if i > 0 and b1[i - 1][j] == 'O':
                    DFS(b1, i - 1, j)
                if i < height - 1 and b1[i + 1][j] == 'O':
                    DFS(b1, i + 1, j)
                if j < width - 1 and b1[i][j + 1] == 'O':
                    DFS(b1, i, j + 1)
                if j > 0 and b1[i][j - 1] == 'O':
                    DFS(b1, i, j - 1)

        height = len(board)
        if height != 0:
            width = len(board[0])
            for i in range(height):
                for j in range(width):
                    if (i == 0 or i == (height - 1) or j == 0 or j == (width - 1)) and board[i][j] == 'O':
                        DFS(board, i, j)

            for i in range(height):
                for j in range(width):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    if board[i][j] == 'N':
                        board[i][j] = 'O'
        self.b = board


s1 = Solution()
s1.solve([["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
          ["O", "X", "O", "X", "O", "X"]])
# s1.solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']])\
# s1.solve([])
print(s1.b)

# Mainly requires the skill on DFS.
# 深度遍历就是选择一个方向然后一直深入直到不满足条件。这道题是只要找到边界的'O'以及链接边界的其他'O'。第一步就过滤掉非边界的'O'
# 然后用DFS迭代找到链接的其他的'O'（这里的顺序是Down->Up->Right->Left），这样就可以完成所有查询。
