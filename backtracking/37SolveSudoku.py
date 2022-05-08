# 编写一个程序，通过填充空格来解决数独问题。
#
# 数独的解法需 遵循如下规则：
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#

# 注意，此时回溯需要返回值。因为相当于多层回溯，外层是位置，内层是1-9的数字，当回溯返回为true时，说明该组合正确，如果回溯返回为false，说明
# 后面肯定出现了无法填补的结果，所以需要退回，即把前面的填过的位置置'.'

class Solution:
    def isValid(self, board, row, col, num):
        # 同行
        for i in range(9):
            if board[row][i] == str(num):
                return False

        # 同列
        for i in range(9):
            if board[i][col] == str(num):
                return False

        # 同一个九宫格
        # 判断同一九宫格是否有冲突
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(num):
                    return False

        return True

    def backtracking(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    continue
                for num in range(1, 10):
                    if not self.isValid(board, row, col, num):
                        continue
                    board[row][col] = str(num)
                    if self.backtracking(board):
                        return True
                    board[row][col] = "."
                return False
        return True

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solu = Solution()
solu.backtracking(board)
print(board)