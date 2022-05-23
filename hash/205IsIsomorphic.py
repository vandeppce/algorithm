# 给定两个字符串 s 和 t ，判断它们是否是同构的。
#
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
#
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
#

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isoHash = {}
        for i in range(len(s)):
            if s[i] not in isoHash.keys():
                if t[i] not in isoHash.values():  # 这一步很关键，防止出现多对一的映射
                    isoHash[s[i]] = t[i]
                else:
                    return False
            else:
                if isoHash[s[i]] != t[i]:
                    return False
        return True