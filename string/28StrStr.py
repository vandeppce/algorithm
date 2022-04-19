# 实现 strStr() 函数。
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
# 如果不存在，则返回  -1 。
#

haystack = "hello"
needle = "ll"
haystack = "aaaaa"
needle = "bba"
haystack = "a"
needle = "ab"

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
def strStr(haystack, needle):
    pass

print(strStr(haystack, needle))