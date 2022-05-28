# 在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。
#
# 给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
#
# 注意：分割得到的每个字符串都必须是平衡字符串，且分割得到的平衡字符串是原平衡字符串的连续子串。
#
# 返回可以通过分割得到的平衡字符串的 最大数量 。
#

s = "RLRRLLRLRL"
# 简单贪心
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        s = list(s)
        countR = 0
        countL = 0
        for c in s:
            if c == "R":
                countR += 1
            else:
                countL += 1
            if countR == countL:
                total += 1
                countR = 0
                countL = 0
        return total