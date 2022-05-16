# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#

prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
"""
# 动规一，五种状态
def maxProfit(prices):
    dp = [[0] * 5 for _ in range(len(prices))]
    # 不操作
    dp[0][0] = 0
    # 第一次买入
    dp[0][1] = -prices[0]
    # 第一次卖出
    dp[0][2] = 0
    # 第二次买入
    dp[0][3] = -prices[0]
    # 第二次卖出
    dp[0][4] = 0

    for i in range(1, len(prices)):
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
        dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
    print(dp)
    return dp[-1]
"""

# 动规二，四种状态
def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 4 for _ in range(len(prices))]
        # 第一次买入
        dp[0][0] = -prices[0]
        # 第一次卖出
        dp[0][1] = 0
        # 第二次买入
        dp[0][2] = -prices[0]
        # 第二次卖出
        dp[0][3] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], 0 - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])
        return dp[-1][-1]

"""
# 二刷
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 4 for _ in range(len(prices))]
        dp[0][0] = dp[0][2] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])
        return dp[-1][3]
"""
print(maxProfit(prices))