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

print(minDistance(word1, word2))