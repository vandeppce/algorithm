# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

class Solution:
    def __init__(self):
        self.path = ""
        self.res = []
    def backtracking(self, left, right):
        if not left and not right:
            self.res.append(self.path)
            return
        if right < left:
            return
        if left:
            left -= 1
            self.path += "("
            self.backtracking(left, right)
            self.path = self.path[:-1]
            left += 1
        if right:
            right -= 1
            self.path += ")"
            self.backtracking(left, right)
            self.path = self.path[:-1]
            right += 1
    def generateParenthesis(self, n: int) -> List[str]:
        self.backtracking(n, n)
        return self.res