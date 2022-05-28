# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
#
# 返回符合要求的 最少分割次数 。


# 先判断s[i][j]是否为回文串。
# dp[i]：范围是[0, i]的回文子串，最少分割次数是dp[i]。
#
# 确定递推公式
# 来看一下由什么可以推出dp[i]。
#
# 如果要对长度为[0, i]的子串进行分割，分割点为j。
#
# 那么如果分割后，区间[j + 1, i]是回文子串，那么dp[i] 就等于 dp[j] + 1。
s = "aabc"
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

"""
# 另一种
# cnt[i]记录到第i个元素时最少需要分割次数，将已遍历元素存在box中，则考虑以下几种情况：
# s[i]不在box中，说明是新元素，则cnt[i]=cnt[i-1]+1
# box+s[i]成为回文串，则cnt[i]=0
# 若在i之前存在最近的k，使cnt[k-1]>cnt[k]，说明在k位置时构成了一个新的回文长串，
# 因此重新计算k之后到i的s串是否构成回文，如果是，则cnt[i]可能的值为cnt[k]+1，记为a
# 并且，对于每一个s[i]，寻找box中距离它最远的可以构成回文串的位置t，则cnt[i]可能的值为cnt[t]+1，记为b
# cnt[i] = min(a, b)

box = s[0]
length = len(s)
cnt = [0] * length
for i in range(1, length):
    if not s[i] in box:
        cnt[i] = cnt[i - 1] + 1
    else:
        x = box + s[i]
        if x[::-1] == x:
            cnt[i] = 0
        else:
            a = ""
            m = cnt[i - 1] + 1
            flag = 0
            for k in range(i - 1, -1, -1):
                if cnt[k] < cnt[k - 1]:
                    a = box[k + 1:] + s[i]
                    break
            if a != "" and a[::-1] == a:
                m = cnt[k] + 1
            for j in range(len(box)):
                if box[j] == s[i]:
                    tmp = box[j:] + s[i]
                    if tmp == tmp[::-1]:
                        flag = 1
                        if j == 0:
                            cnt[i] = 0
                        else:
                            cnt[i] = min(cnt[j - 1] + 1, cnt[i - 1] + 1, m)
                        break
            if flag == 0:
                cnt[i] = cnt[i - 1] + 1
    box += s[i]
print(cnt)
"""
print(minCut(s))