# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
#
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
#
# 返回 你能获得的 最大 利润 。
#

# 贪心算法，只要明天价格比今天高，那么就今天买明天卖
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(0, len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                total += diff
        return total