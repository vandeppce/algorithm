s = "aab"

def minCut(s):
    isPalindromic = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        isPalindromic[i][i] = 1
    for i in range(len(s) - 2, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                isPalindromic[i][j] = 0
            else:
                if j == i + 1 or isPalindromic[i + 1][j - 1] == 1:
                    isPalindromic[i][j] = 1
    dp = [len(s)] * len(s)
    dp[0] = 0
    for i in range(1, len(s)):
        if isPalindromic[0][i] == 1:
            dp[i] = 0
            continue
        for j in range(i):
            if isPalindromic[j + 1][i] == 1:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]

print(minCut(s))