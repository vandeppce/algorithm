# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

# 通过hash来记录字符是否已经出现，对于只出现了一次的字符添加到list中，当再次出现时从list中删除，最后返回list的第一个元素即可
class Solution:
    def firstUniqChar(self, s: str) -> str:
        charHash = {}
        stack = []
        for c in s:
            if charHash.get(c, -1) == -1:
                stack.append(c)
                charHash[c] = 1
            else:
                if charHash[c] > 0:
                    stack.remove(c)
                    charHash[c] -= 1
        if stack:
            return stack[0]
        else:
            return ' '