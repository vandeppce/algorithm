# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
# s = "bbbbb"
# s = "pww"
s = "abcabcbb"
s = "pwwkewabcdf"
# 滑动窗口法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cHash = {}
        s = list(s)
        maxLength = 0
        startIdx = 0
        for i, c in enumerate(s):
            if cHash.get(c, -1) == -1:
                cHash[c] = i
            else:
                maxLength = max(maxLength, i - startIdx)
                startIdx = cHash[c] + 1
                for k, v in cHash.items():
                    if v < startIdx - 1:
                        cHash[k] = -1
                cHash[c] = i
        return max(maxLength, len(s) - startIdx)

# 双指针+哈希表
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res

# 动态规划+哈希表
# dp[i]表示以s[i]为结尾的最长不重复子串长度
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

solu = Solution()
print(solu.lengthOfLongestSubstring(s))