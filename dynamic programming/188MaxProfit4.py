# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#

k = 2
prices = [3,2,6,5,0,3]

def maxProfit(k, prices):
    if len(prices) <= 1 or k == 0:
        return 0
    dp = [[0] * 2 * k for _ in range(len(prices))]
    i = 0
    while i < 2 * k:
        dp[0][i] = -prices[0]
        i += 2

    for i in range(1, len(prices)):
        for j in range(2 * k):
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], -prices[i])
            elif j % 2 == 1:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
    return dp[-1][-1]

print(maxProfit(k, prices))