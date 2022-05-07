# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#

class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def isValid(self, row, col, board):
        # 同一列
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        # 同一行，不需要判断，因为每一行填了Q以后直接到下一行

        # 左上对角线
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 右上对角线
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
            temp_res = []
            for temp in board:
                temp_str = "".join(temp)
                temp_res.append(temp_str)
            self.res.append(temp_res)
            return # 这里也可以不要return，反正当row=n这一行时，肯定找不到合适的Q，循环结束后自动回到递归上一层
        for col in range(n):
            if not self.isValid(row, col, board):
                continue
            board[row][col] = "Q"
            self.backtracking(row + 1, n, board)
            board[row][col] = '.'

    def solveNQueens(self, n: int):
        board = [['.'] * n for _ in range(n)]
        self.backtracking(0, n, board)
        return self.res

n = 4
solu = Solution()
print(solu.solveNQueens(n))