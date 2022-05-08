# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，
# 同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

S = "ababcbacadefegdehijhklij"

# 查看每个字符是否在前面已出现，并且合并其出现的序列至当前，更新序列id及各元素出现的序列id
def partitionLabels(s):
    hasChrs = {}
    hasSequences = []
    for i, chr in enumerate(s):
        if chr not in hasChrs.keys():
            hasChrs[chr] = len(hasSequences)
            hasSequences.append(chr)
        else:
            chrIdx = hasChrs[chr]
            updateSequences = "".join(hasSequences[chrIdx:]) + chr
            hasSequences = hasSequences[:chrIdx]
            hasSequences.append(updateSequences)
            for key, value in hasChrs.items():
                if value >= chrIdx:
                    hasChrs[key] = chrIdx

    lens = []
    for sequence in hasSequences:
        lens.append(len(sequence))
    return lens

"""
# 二刷，差不多，主要是记录当前字符在已划分字符串序列中的索引，并合并该子串及其之后所有串，同时更新索引
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chrDict = {}
        strs = []
        s = list(s)
        for i, chr in enumerate(s):
            if chr not in chrDict.keys():
                chrDict[chr] = len(strs)
                strs.append(chr)
            else:
                tmp = ""
                idx = chrDict[chr]
                for c in strs[idx:]:
                    tmp += c
                strs = strs[:idx]
                strs.append(tmp + chr)
                for k, v in chrDict.items():
                    if v >= idx:
                        chrDict[k] = idx
        res = []
        for item in strs:
            res.append(len(item))
        return res
"""
print(partitionLabels(S))