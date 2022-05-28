# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
#

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = [""]
strs = ["a"]
def groupAnagrams(strs):
    dicts = []
    res = []

    for str in strs:
        hashTable = {}
        for chr in str:
            if chr not in hashTable:
                hashTable[chr] = 1
            else:
                hashTable[chr] += 1
        if hashTable not in dicts:
            dicts.append(hashTable)
            res.append([str])
        else:
            index = dicts.index(hashTable)
            res[index].append(str)
    return res

print(groupAnagrams(strs))