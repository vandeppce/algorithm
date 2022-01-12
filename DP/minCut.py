# 分割回文串 II
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
#
# 返回符合要求的 最少分割次数 。
#
#  
#
# 示例 1：
#
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

s = "aab"
box = ""
length = len(s)
cnt = 0
for i in range(length):
    if not s[i] in box:

    box.append(s[i])