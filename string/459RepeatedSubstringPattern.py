# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。

s = "abab"
s = "aba"
s = "abcabcabcabc"
s = "aaa"
s = "ababab"

'''
# 枚举法
def repeatedSubstringPattern(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        if s == s[:i] * (length // i):
            return True
    return False
'''

# KMP
def repeatedSubstringPattern(s):
    pass

print(repeatedSubstringPattern(s))