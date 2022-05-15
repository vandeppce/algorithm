# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
#
# 回文字符串 是正着读和倒过来读一样的字符串。
#
# 子字符串 是字符串中的由连续字符组成的一个序列。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
#

s = "abc"
s = "aaa"
# 动规一，遍历到每个位置时，判断包含其的所有子串是否回文
def countSubstrings(s):
    dp = [1] * len(s)
    for i in range(1, len(s)):
        dp[i] += dp[i - 1]
        for j in range(i):
            tmp = s[j: i + 1]
            if tmp == tmp[::-1]:
                dp[i] += 1
    print(dp)
    return dp[-1]

# 动规二，使用二维数组，dij表示i到j是不是回文
# 在确定递推公式时，就要分析如下几种情况。
# 整体上是两种，就是s[i]与s[j]相等，s[i]与s[j]不相等这两种。
# 当s[i]与s[j]不相等，dp[i][j]一定是false。
# 当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况
# 情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
# 情况二：下标i 与 j相差为1，例如aa，也是回文子串
# 情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，
# 我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，
# 这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        # 外层一定要从下到上遍历
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j]:
                        res += 1
        return res
print(countSubstrings(s))