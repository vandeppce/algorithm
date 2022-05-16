# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
#
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
# （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
#
# 题目数据保证答案符合 32 位带符号整数范围。
#

s = "rabbbit"
t = "rabbit"
s = "babgbag"
t = "bag"
# dp[i][j]：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]。
#
# 确定递推公式
# 这一类问题，基本是要分析两种情况
#
# s[i - 1] 与 t[j - 1]相等
# s[i - 1] 与 t[j - 1] 不相等
# 当s[i - 1] 与 t[j - 1]相等时，dp[i][j]可以有两部分组成。
# 一部分是用s[i - 1]来匹配，那么个数为dp[i - 1][j - 1]。
# 一部分是不用s[i - 1]来匹配，个数为dp[i - 1][j]。
# 例如： s：bagg 和 t：bag ，s[3] 和 t[2]是相同的，但是字符串s也可以不用s[3]来匹配，即用s[0]s[1]s[2]组成的bag。
# 当然也可以用s[3]来匹配，即：s[0]s[1]s[3]组成的bag。
# 所以当s[i - 1] 与 t[j - 1]相等时，dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
# 当s[i - 1] 与 t[j - 1]不相等时，dp[i][j]只有一部分组成，不用s[i - 1]来匹配，即：dp[i - 1][j]
# 所以递推公式为：dp[i][j] = dp[i - 1][j];

def numDistinct(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][0] = 1

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    return dp[-1][-1]

print(numDistinct(s, t))