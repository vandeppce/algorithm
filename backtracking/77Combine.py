# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracking(self, n, k, start):
        if len(self.path) == k:
            self.res.append(self.path[:])
            return

        for i in range(start, n + 1):
            self.path.append(i)
            self.backtracking(n, k, i + 1)
            self.path.pop()

    def combine(self, n: int, k: int):
        self.backtracking(n, k, 1)
        return self.res

solu = Solution()
print(solu.combine(4, 2))