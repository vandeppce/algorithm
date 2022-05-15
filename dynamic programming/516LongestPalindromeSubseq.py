# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
#

s = "bbbab"
s = "cbbd"

def longestPalindromeSubseq(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                # 说明首位相等，则在去掉首位后的子串+2
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # 说明首位不等，有两种可能，去掉首或去掉尾，选较大值
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    print(dp)
    return dp[0][-1]

print(longestPalindromeSubseq(s))