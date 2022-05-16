# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
#
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#
# 返回获得利润的最大值。
#
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
#
# dp[0]的初始化，初始收益应该是0
prices = [1, 3, 2, 8, 4, 9]
fee = 2
# prices = [1,3,7,5,10,3]
# fee = 3
prices = [9,8,7,1,2]
fee = 3
"""
# 动规一，卖出收费
def maxProfit(prices):
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0]
    # dp[0][1] = -fee # 第一天卖出股票后的剩余现金不能为-fee，而应该是0
    dp[0][1] = 0

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
    print(dp)
    return dp[-1][1]
"""

# 动规二，买入收费
def maxProfit(prices):
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0] - fee
    # dp[0][1] = -fee # 第一天卖出股票后的剩余现金不能为-fee，而应该是0
    dp[0][1] = 0

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i] - fee)
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
    print(dp)
    return dp[-1][1]
print(maxProfit(prices))