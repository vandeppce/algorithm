# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#

# 背包问题总结
# 递推公式
# 问能否能装满背包（或者最多装多少）：dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]);
# 问装满背包有几种方法：dp[j] += dp[j - nums[i]]
# 问背包装满最大价值：dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
# 问装满背包所有物品的最小个数：dp[j] = min(dp[j - coins[i]] + 1, dp[j])

# 遍历顺序
# 01背包，一维dp数组01背包只能先遍历物品再遍历背包容量，且第二层for循环是从大到小遍历
# 完全背包，如果求组合数（不考虑顺序）就是外层for循环遍历物品，内层for遍历背包。如果求排列数就是外层for遍历背包，内层for循环遍历物品。
'''
# 回溯，超时
class Solution:
    def __init__(self):
        self.path = ""
    def backtracking(self, s, wordDict):
        if len(self.path) >= len(s):
            if self.path == s:
                return True
            return False

        for i in range(len(wordDict)):
            self.path += wordDict[i]
            if self.backtracking(s, wordDict):
                return True
            self.path = self.path[:-len(wordDict[i])]
        return False

    def wordBreak(self, s: str, wordDict) -> bool:
        return self.backtracking(s, wordDict)
solu = Solution()
print(solu.wordBreak(s, wordDict))
'''

s = "leetcode"
wordDict = ["leet", "code"]
s = "applepenapple"
wordDict = ["apple", "pen"]
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

# 对于一个串，如果dp[i-j]可以由词组构成，并且dp[i-j:i]也在词组中，那么dp[i]可以由词组构成
def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    '''
    # 一种动规方式，遍历i位置前所有的子串
    for i in range(1, len(s) + 1):
        for j in range(i):
            word = s[j: i]
            if word in wordDict and dp[j] == True:
                dp[i] = True
                break
    print(dp)
    return dp[-1]
    '''

    # 第二种动规方式，遍历词组，和i前的子串匹配
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if dp[i - len(word)] == True and s[i - len(word): i] == word:
                dp[i] = True
    print(dp)
    return dp[-1]

"""
# 二刷，差不多，注意这里外层一定是遍历字符串s的位置
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for word in wordDict:
                if i >= len(word):
                    if dp[i - len(word)] and s[i - len(word): i] == word:
                        dp[i] = True
        return dp[-1]
"""
print(wordBreak(s, wordDict))