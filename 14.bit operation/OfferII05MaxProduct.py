# 给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。
# 假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
#

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        elements = [[0] * 26 for _ in range(len(words))]
        res = 0
        for i in range(len(words)):
            for c in words[i]:
                elements[i][ord(c) - ord('a')] = 1
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                flag = 1
                for k in range(26):
                    if elements[i][k] & elements[j][k]:
                        flag = 0
                        break
                if flag:
                    res = max(res, len(words[i] * len(words[j])))
        return res