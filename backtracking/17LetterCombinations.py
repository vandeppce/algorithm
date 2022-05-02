# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#

class Solution:
    def __init__(self):
        self.path = ""
        self.res = []
        self.table = {'2': 'abc',
                      '3': 'def',
                      '4': 'ghi',
                      '5': 'jkl',
                      '6': 'mno',
                      '7': 'pqrs',
                      '8': 'tuv',
                      '9': 'wxyz'}

    def backtracking(self, digits):
        if not digits:
            if self.path:
                self.res.append(self.path)
            return

        curr_digit = digits[0]
        for i in range(len(self.table[curr_digit])):
            self.path += self.table[curr_digit][i]
            self.backtracking(digits[1:])
            self.path = self.path[:-1]

    def letterCombinations(self, digits: str):
        self.backtracking(digits)
        return self.res