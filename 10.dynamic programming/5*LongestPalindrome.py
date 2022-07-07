# 给你一个字符串 s，找到 s 中最长的回文子串。

s = "babad"
s = "cbbd"
s = "aacabdkacaa"
# 动态规划，记录s[i:j]是否回文
def longestPalindrome(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    maxL = 1
    maxI = 0
    maxJ = 0

    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s) - 2, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if j == i + 1:
                    dp[i][j] = 2
                else:
                    if dp[i + 1][j - 1] != 0:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                if dp[i][j] > maxL:
                    maxL = dp[i][j]
                    maxI = i
                    maxJ = j
    print(dp)
    return s[maxI:maxJ + 1]

print(longestPalindrome(s))