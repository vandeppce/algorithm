# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
# 回溯
s = "abc"
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def backtracking(self, s):
        if not s:
            self.res.append("".join(self.path))
            return
        usedList = []
        for i in range(len(s)):
            if s[i] in usedList:
                continue
            usedList.append(s[i])
            self.path.append(s[i])
            tmp = s.pop(i)
            self.backtracking(s)
            s.insert(i, tmp)
            self.path.pop()

    def permutation(self, s: str) -> List[str]:
        s = list(s)
        self.backtracking(s)
        return self.res