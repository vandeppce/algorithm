# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
#
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
#
# 返回 你能获得的 最大 利润 。
#

prices = [7,1,5,3,6,4]
"""
# 动规一
def maxProfit(prices):
    dp = [0] * len(prices)
    for i in range(1, len(prices)):
        dp[i] = dp[i - 1] + max(0, prices[i] - prices[i - 1])
    print(dp)
    return dp[-1]
"""

# 动规二
def maxProfit(prices):
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0]
    dp[0][1] = 0

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
    print(dp)
    return dp[-1]
print(maxProfit(prices))