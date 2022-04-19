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