s = "cbaebabacd"
p = "abc"
s = "abab"
p = "ab"
class Solution:
    def findAnagrams(self, s: str, p: str):
        need = {}
        res = []
        for c in p:
            need[c] = need.get(c, 0) + 1
        needLength = len(p)

        for i, c in enumerate(list(s)):
            if i > len(p) - 1 and s[i - len(p)] in need.keys():
                need[s[i - len(p)]] += 1
                if need[s[i - len(p)]] > 0:
                    needLength += 1

            if c in need.keys():
                need[c] -= 1
                if need[c] >= 0:
                    needLength -= 1

            if not needLength:
                res.append(i - len(p) + 1)
        return res

solu = Solution()
print(solu.findAnagrams(s, p))