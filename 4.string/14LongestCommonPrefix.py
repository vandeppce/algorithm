# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for str in strs[1:]:
                if len(str) > i and str[i] == c:
                    continue
                else:
                    return res
            res += c
        return res