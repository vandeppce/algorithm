# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
#
#  
#
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
#

# n个骰子共有5n+1种组合
# 设dp[i][j]为i个骰子和为j的情况，由于第i个骰子分别可以取值为1,2,3,4,5,6
# 所以其总数为dp[i-1][j-1]+dp[i-1][j-2]+...+dp[i-1][j-6]

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1] * 6
        baseProb = 1 / 6 ** n
        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(tmp)):
                tmp[j] = sum(dp[max(0, j - 5): j + 1])
            dp = tmp
        for i in range(len(dp)):
            dp[i] *= baseProb
        return dp