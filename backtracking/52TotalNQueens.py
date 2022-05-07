# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

class Solution:
    def __init__(self):
        self.res = 0

    def isValid(self, row, col, board):
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtracking(self, row, n, board):
        if row == n:
            self.res += 1

        for col in range(n):
            if not self.isValid(row, col, board):
                continue
            board[row][col] = 'Q'
            self.backtracking(row + 1, n, board)
            board[row][col] = '.'

    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        self.backtracking(0, n, board)
        return self.res