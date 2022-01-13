# 两个字符串的删除操作
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
#
#  
#
# 示例：
#
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

word1 = "sea"
word2 = "eat"

# word1 = "acbcbcef"
# word2 = "abcbced"

# word1 = "park"
# word2 = "spake"

# word1 = "leetcode"
# word2 = "etco"
# 最长公共子串，not ac，在"park"和"spake"题出错。本题应该是最长公共子序列问题

'''
length1 = len(word1)
length2 = len(word2)

dp = [[0] * length2 for _ in range(length1)]
max_length = 0

for i in range(length1):
    for j in range(length2):
        if word1[i] == word2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
            max_length = max(dp[i][j], max_length)

print(max_length)
print(length1 + length2 - 2 * max_length)
'''

# 最长公共子序列，动态规划。若匹配，则dp[i][j]=dp[i-1][j-1]+1, 若不匹配则dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
length1 = len(word1)
length2 = len(word2)

dp = [[0] * length2 for _ in range(length1)]

for i in range(length1):
    for j in range(length2):
        if word1[i] == word2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            if i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp)