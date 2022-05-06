# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracking(self, s, start):
        if start >= len(s):
            self.res.append(self.path[:])
            return # return行可以不要

        for i in range(start, len(s)):
            substr = s[start: i + 1]
            if substr == substr[::-1]:
                self.path.append(substr)
                self.backtracking(s, i + 1)
                self.path.pop()

    def partition(self, s: str):
        self.backtracking(s, 0)
        return self.res

"""
# 二刷，直接操作s
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    
    def backtracking(self, s):
        if not s:
            self.res.append(self.path[:])
            return

        for i in range(len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                self.path.append(s[:i + 1])
                self.backtracking(s[i + 1:])
                self.path.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s)
        return self.res
"""
s = "aab"
solu = Solution()
print(solu.partition(s))