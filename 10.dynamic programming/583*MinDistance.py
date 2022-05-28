# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
#
# 每步 可以删除任意一个字符串中的一个字符。

word1 = "sea"
word2 = "eat"
word1 = "leetcode"
word2 = "etco"
# 求最长公共子序列
def minDistance(word1, word2):
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return len(word1) + len(word2) - 2 * dp[-1][-1]

"""
# 二刷，另一种动规方案
# dp[i][j]：以i-1为结尾的字符串word1，和以j-1位结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。
# 当word1[i - 1] 与 word2[j - 1]相同的时候，dp[i][j] = dp[i - 1][j - 1];
# 当word1[i - 1] 与 word2[j - 1]不相同的时候，有三种情况：
# 情况一：删word1[i - 1]，最少操作次数为dp[i - 1][j] + 1
# 情况二：删word2[j - 1]，最少操作次数为dp[i][j - 1] + 1
# 情况三：同时删word1[i - 1]和word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 2

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for i in range(len(word1) + 1):
            dp[i][0] = i
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 2)
        return dp[-1][-1]
"""
print(minDistance(word1, word2))