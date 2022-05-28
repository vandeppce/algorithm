# 实现 strStr() 函数。
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
# 如果不存在，则返回  -1 。
#

haystack = "hello"
needle = "ll"
haystack = "a"
needle = "ab"
haystack = "aaaaa"
needle = "bba"
haystack = "aabaabaaf"
needle = "aabaaf"

'''
# 暴力搜索
def strStr(haystack, needle):
    lenH = len(haystack)
    lenN = len(needle)

    for i in range(0, lenH - lenN + 1):
        if haystack[i: i + lenN] == needle:
            return i
    return -1
'''

# KMP
def getNext(needle):
    length = len(needle)
    next = [0] * length
    for i in range(length):
        for j in range(i, 0, -1):
            # 前缀 needle[:j]
            # 后缀 needle[i - j + 1: i + 1]
            if needle[:j] == needle[i - j + 1: i + 1]:
                next[i] = j
                break
    return next

def strStr(haystack, needle):
    next = getNext(needle)
    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = next[j - 1]
            else:
                i += 1
        if j == len(needle):
            return i - j
    return -1

print(strStr(haystack, needle))

"""
# 二刷，重点是构造getnext数组
def getnext(needle):
    next = [0] * len(needle)
    j = 0
    for i in range(1, len(needle)):
        while (j > 0 and needle[i] != needle[j]):
            j = next[j - 1]
            # j -= 1 也可
        if (needle[i] == needle[j]):
            j += 1
        next[i] = j
    return next

def strStr(haystack: str, needle: str) -> int:
    hIndex = 0
    nIndex = 0
    nxt = getnext(needle)
    if needle == "":
        return 0
    while hIndex < len(haystack):
        if haystack[hIndex] == needle[nIndex]:
            hIndex += 1
            nIndex += 1

            if nIndex == len(needle):
                return hIndex - len(needle)
        else:
            if nIndex == 0:
                hIndex += 1
            else:
                nIndex = nxt[nIndex - 1]
    return -1
print(strStr(haystack, needle))
"""

"""
# 三刷
class Solution:
    def getNext(self, needle):
        next = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = next[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next[i] = j
        return next
    def strStr(self, haystack: str, needle: str) -> int:
        next = self.getNext(needle)
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = next[j - 1]
                else:
                    i += 1
            if j == len(needle):
                return i - j
        return -1
"""