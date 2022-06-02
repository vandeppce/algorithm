# 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
#
# 动态规划，dp[i][j]代表s[:i]和p[:j]是否可以匹配
# 递推公式，分成p[j-1]='*'和p[j-1]!='*'
# p[j-1]='*'时，有三种情况可以使得dp[i][j]=True
# 1. dp[i][j-2]=True，也就是p[j-2]*出现0次，例如a和ab*。
# 2. dp[i-1][j]=True且s[i-1]=p[j-2]，也就是让字符p[j-2]多出现1次，例如abb和ab*，ab和ab*可以匹配，此时b出现1次，abb和ab*也可以匹配，此时b出现两次。
# 3. dp[i-1][j]=True且p[j-2]='.'，'.'可以当作任何字符，自然也可以当作s[i-1]，例如abb和a.*
# p[j-1]!='*'时，有两种情况可以使得dp[i][j]=True
# 1. s[i-1]=p[j-1]且dp[i-1][j-1]=True
# 2. p[j-1]=True且dp[i-1][j-1]=True
# 初始化时，要初始化为+1行和列，首行表示空字符匹配。
# dp[0][0]=True，代表两个空字符可以匹配
# dp[0][j]=dp[0][j-2]且p[j-1]='*'，也就是让奇数位出现0次，保持p为空字符，可以和空字符匹配

s = "aaa"
p = "ab*.*"

def isMatch(s, p):
    dp = [[0] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = 1
    for j in range(2, len(p) + 1, 2):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
            else:
                if dp[i][j - 2] == 1:
                    dp[i][j] = 1
                elif dp[i - 1][j] == 1 and s[i - 1] == p[j - 2]:
                    dp[i][j] = 1
                elif dp[i - 1][j] == 1 and p[j - 2] == '.':
                    dp[i][j] = 1
    return dp[-1][-1]

print(isMatch(s, p))