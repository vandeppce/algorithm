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

print(partitionLabels(S))