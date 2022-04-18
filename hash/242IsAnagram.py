# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
#

s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

def isAnagram(s, t):
    hashS = {}
    hashT = {}

    for chr in s:
        if chr not in hashS.keys():
            hashS[chr] = 1
        else:
            hashS[chr] += 1

    for chr in t:
        if chr not in hashT.keys():
            hashT[chr] = 1
        else:
            hashT[chr] += 1

    return hashT == hashS


print(isAnagram(s, t))