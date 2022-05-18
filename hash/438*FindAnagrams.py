# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
# 另一种方法是滑动窗口

s = "cbaebabacd"
p = "abc"
s = "abab"
p = "ab"
s = "aaaaaaaaaa"
p = "aaaaaaaaaaaaa"
def findAnagrams(s: str, p: str):
    lengthS = len(s)
    lengthP = len(p)

    hashP = {}
    ret = []

    # 利用p构造字典
    for chr in p:
        if chr not in hashP:
            hashP[chr] = 1
        else:
            hashP[chr] += 1

    if lengthS < lengthP:
        return []

    end = lengthS - (lengthP - 1)
    prev = 0
    prev_str = ""

    for i in range(end):
        str = s[i: i + lengthP]
        flag = 0
        tmp_hash = hashP.copy()

        # 如果前一个是异位词，那么如果当前串的最后一位和前串第一位一样，则当前串也是异位词
        if prev == 1:
            if str[-1] == prev_str[0]:
                prev = 1
                prev_str = str
                ret.append(i)
                continue

        # 如果前串非异位词，那么如果当前串的最后一位和前串第一位一样，则当前串也非异位词
        if prev == 0 and prev_str != "":
            if prev_str[0] in hashP.keys():
                if prev_str[0] == str[-1]:
                    prev = 0
                    prev_str = str
                    continue

        # 正常比较两个串
        for chr in str:
            if chr not in hashP.keys():
                flag = 1
                break
            else:
                tmp_hash[chr] -= 1
                if tmp_hash[chr] < 0:
                    flag = 1
                    break

        if not flag:
            prev = 1
            ret.append(i)
        else:
            prev = 0
        prev_str = str

    return ret


print(findAnagrams(s, p))

"""
# 二刷
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashP = {}
        res = []
        if len(s) < len(p):
            return res
            
        for chrP in p:
            hashP[chrP] = hashP.get(chrP, 0) + 1
        
        slow = 0
        fast = 0
        for i in range(len(p)):
            if s[i] in hashP.keys():
                hashP[s[i]] -= 1
            fast += 1
        flag = 0
        for k, v in hashP.items():
            if v != 0:
                flag = 1
                break
        if not flag:
            res.append(0)

        while fast < len(s):
            outChr = s[slow]
            inChr = s[fast]
            slow += 1
            fast += 1
            if outChr in hashP.keys():
                hashP[outChr] += 1
            if inChr in hashP.keys():
                hashP[inChr] -= 1
            flag = 0
            for k, v in hashP.items():
                if v != 0:
                    flag = 1
                    break
            if not flag:
                res.append(slow)
        return res
"""
"""
# 三刷
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        res = []
        for c in p:
            need[c] = need.get(c, 0) + 1
        needLength = len(p)

        for i, c in enumerate(list(s)):
            if i > len(p) - 1 and s[i - len(p)] in need.keys():
                need[s[i - len(p)]] += 1
                needLength += 1

            if c in need.keys():
                need[c] -= 1
                needLength -= 1

            if sum(need.values()) == 0 and max(need.values()) == 0:
                res.append(i - len(p) + 1)
        return res
"""

"""
# 或者只有当删除或添加字符>0时才操作needLength，就是为了防止bab这种情况
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        res = []
        for c in p:
            need[c] = need.get(c, 0) + 1
        needLength = len(p)

        for i, c in enumerate(list(s)):
            if i > len(p) - 1 and s[i - len(p)] in need.keys():
                need[s[i - len(p)]] += 1
                if need[s[i - len(p)]] > 0:
                    needLength += 1

            if c in need.keys():
                need[c] -= 1
                if need[c] >= 0:
                    needLength -= 1

            if not needLength:
                res.append(i - len(p) + 1)
        return res
"""