# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#

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

print(wordBreak(s, wordDict))