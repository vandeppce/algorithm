# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [5,8,7,3,6,4]

'''
# 动规一
def maxProfit(prices):
    dp = [0] * len(prices)
    for i in range(1, len(prices)):
        dp[i] = max(0, dp[i - 1] + (prices[i] - prices[i - 1]))
    print(dp)
    return max(dp)
'''

# 动规二
def maxProfit(prices):
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0]
    dp[0][1] = 0

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], -prices[i])
        dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])
    return dp[-1]
print(maxProfit(prices))