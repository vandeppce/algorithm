# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
# （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#
# 进阶：
#
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
#

s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdc"

# 求公共子序列
def isSubsequence(s, t):
    if s == "":
        return True
    l1 = len(s)
    l2 = len(t)
    dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
    for i in range(1, l2 + 1):
        for j in range(1, l1 + 1):
            if t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if dp[i][j] == l1:
                return True
    return False

# 求编辑距离，s为列，t为行。不和上比较，只和左比较，这样的原因是要查看s是否包含在t中，所以当s[i - 1]和t[j - 1]不想等时，
# 上一个s[i - 2]的信息没有用

def isSubsequence(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]
    if dp[-1][-1] == len(s):
        return True
    return False

# 二刷，s为列，t为行。不和上比较，只和左比较，标志位为True or False
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[False] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(t) + 1):
            dp[0][i] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1] and dp[i - 1][j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]

print(isSubsequence(s, t))