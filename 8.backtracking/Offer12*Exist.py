# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#  
#
# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
#

class Solution:
    def backtracking(self, board, i, j, word, start, hasSeen):
        if start >= len(word):
            return True
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
            return False
        if hasSeen[i][j] == 1:
            return False
        if board[i][j] != word[start]:
            return False
        hasSeen[i][j] = 1
        ### 注意，下面四个判断才是回溯的过程，如果判断均不通过，那么说明ij位置无法进行下一步匹配，需要回到上层选择下一个点进行遍历，因此最后将
        ### hasSeen[i][j]置为0。
        # 上
        if i > 0:
            if self.backtracking(board, i - 1, j, word, start + 1, hasSeen):
                return True
            # 注意，一定不要在这个位置对hasSeen赋值，因为此时并不知道i-1 j点是否有效
            # hasSeen[i - 1][j] = 0
        # 下
        if i < len(board) - 1:
            if self.backtracking(board, i + 1, j, word, start + 1, hasSeen):
                return True
            # hasSeen[i + 1][j] = 0
        # 左
        if j > 0:
            if self.backtracking(board, i, j - 1, word, start + 1, hasSeen):
                return True
            # hasSeen[i][j - 1] = 0
        # 右
        if j < len(board[0]) - 1:
            if self.backtracking(board, i, j + 1, word, start + 1, hasSeen):
                return True
            # hasSeen[i][j + 1] = 0
        hasSeen[i][j] = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        hasSeen = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    ret = self.backtracking(board, i, j, word, 0, hasSeen)
                    # hasSeen[i][j] = 0
                    if ret:
                        return True
        return False

board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
word = "aaaaaaaaaaaaa"
solu = Solution()
print(solu.exist(board, word))