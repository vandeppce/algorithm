# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
# 另一种方法是滑动窗口

s = "cbaebabacd"
p = "abc"
s = "abab"
p = "ab"

def findAnagrams(self, s: str, p: str) -> List[int]:
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