# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

s = "abcabcbb"
# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        cList = []
        maxLength = 0
        for c in s:
            if c in cList:
                idx = cList.index(c)
                maxLength = max(maxLength, len(cList))
                cList = cList[idx + 1:]
            cList.append(c)
        return max(maxLength, len(cList))