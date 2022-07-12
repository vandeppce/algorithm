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
            self.res.append(self.path)
            return
        num = digits.pop(0)
        cStr = self.table[num]
        for i in range(len(cStr)):
            self.path += cStr[i]
            self.backtracking(digits)
            self.path = self.path[:-1]
        digits.insert(0, num)
    def letterCombinations(self, digits):
        digits = list(digits)
        self.backtracking(digits)
        return self.res

digits = "23"
solu = Solution()
print(solu.letterCombinations(digits))