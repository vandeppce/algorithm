s = "aab"

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

    def partition(self, s: str):
        self.backtracking(s)
        return self.res

solu = Solution()
print(solu.partition(s))
print(int("255"))