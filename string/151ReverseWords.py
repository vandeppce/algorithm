# 给你一个字符串 s ，颠倒字符串中 单词 的顺序。

s = "the sky is blue"
s = "  hello world  "
s = "a good   example"

# 正常方法
def reverseWords(s):
    s_list = s.split(" ")[::-1]
    res = ""
    for s in s_list:
        if s != "":
            res = res + s + " "
    return res[:-1]

print(reverseWords(s))

"""
# 二刷，双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. 移除多余空格
        left = 0
        right = len(s) - 1
        # 开头空格
        while s[left] == " ":
            left += 1
        # 结尾空格
        while s[right] == " ":
            right -= 1
        # 中间空格
        tmp = ""
        while left <= right:
            if s[left] != " ":
                tmp += s[left]
            else:
                if s[left - 1] != " ":
                    tmp += s[left]
            left += 1
        tmp = list(tmp)

        # 2. 字符串反向
        left = 0
        right = len(tmp) - 1

        while left < right:
            sLeft = tmp[left]
            sRight = tmp[right]
            exchange = sLeft
            tmp[left] = sRight
            tmp[right] = exchange

            left += 1
            right -= 1

        # 3. 单词反向
        slow = 0
        fast = 0
        tmp.append(" ")
        while fast < len(tmp):
            if tmp[fast] == " ":
                tmp[slow: fast] = tmp[slow: fast][::-1]
                slow = fast + 1
                fast = slow
            fast += 1
        return "".join(tmp[:-1])
"""