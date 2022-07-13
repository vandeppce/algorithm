# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
#
s = "abcd"
k = 2
s = "abcdefga"
k = 3
s = "abcd"
k = 2
s = "abcdefg"
k = 2

'''
# 设置计数器
def reverseStr(s, k):
    length = len(s)
    cnt = 0
    ends = length % (2 * k)
    for i in range(length - ends):
        cnt += 1
        if cnt == k:
            reverse = s[i - cnt + 1: i + 1][::-1]
            s = s[:i - cnt + 1] + reverse + s[i + 1:]
        if cnt == 2 * k:
            cnt = 0
    if ends <= k:
        reverse = s[length - ends:][::-1]
        s = s[:length - ends] + reverse
    else:
        reverse = s[length - ends: length - ends + k][::-1]
        s = s[:length - ends] + reverse + s[length - ends + k:]
    return s
'''
def reverseStr(s, k):
    length = len(s)
    p = 0
    while p < length:
        p1 = p + k
        s = s[:p] + s[p:p1][::-1] + s[p1:]
        p += 2 * k
    return s

"""
# 二刷
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        p = 0
        s = list(s)
        while p < length:
            s[p: p + 2 * k] = s[p: p + k][::-1] + s[p + k: p + 2 * k]
            p += 2 * k
        return "".join(s)
"""
print(reverseStr(s, k))
