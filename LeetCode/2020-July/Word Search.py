from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        b_flag = [[0] * len(board[0])] * len(board)
        for i in range(board):
            for j in range(board[0]):
                res = self.DFS(board, b_flag, word, i, j, 0)

        return res

    def DFS(self, b, word, i, j, pos):

        if b[i][j] == word[pos]:
            if