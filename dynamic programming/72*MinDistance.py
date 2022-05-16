# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#

word1 = "horse"
word2 = "ros"
word1 = "intention"
word2 = "execution"
def minDistance(word1, word2):
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 替换，由于word1[i-1]已经和word2[j-1]相同，那么dp[i][j]=dp[i - 1][j - 1]+1，即把word1[i]换成word2[j]
                # 删除，由于word1[i-1]已经和word2[j]相同，那么dp[i][j]=dp[i - 1][j]+1，即把word1[i]删除
                # 添加，由于word1[i]和word2[j-1]相同，那么dp[i][j]=dp[i][j-1]+1，即在word1[i+1]位置添加word2[j]
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    print(dp)
    return dp[-1][-1]

print(minDistance(word1, word2))