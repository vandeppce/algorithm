board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

class Solution:
    def isValid(self, row, col, board, i):
        # 同行
        for j in range(9):
            if board[row][j] == i:
                return False

        # 同列
        for j in range(9):
            if board[j][col] == i:
                return False

        # 同一个九宫格
        s_row = (row // 3) * 3
        s_col = (row // 3) * 3
        for j in range(s_row, s_row + 3):
            for k in range(s_col, s_col + 3):
                if board[j][k] == i:
                    return False
        return True

    def backtracking(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    continue
                for i in range(1, 10):
                    if not self.isValid(row, col, board, str(i)):
                        continue
                    board[row][col] = str(i)
                    if self.backtracking(board):
                        return True
                    board[row][col] = '.'
                return False
        return True

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

solu = Solution()
print(solu.backtracking(board))
