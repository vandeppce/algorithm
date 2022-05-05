# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
#
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#
# 返回获得利润的最大值。
#
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
#

prices = [1, 3, 2, 8, 4, 9]
fee = 2
prices = [1,3,7,5,10,3]
fee = 3
# 贪心算法，分三种情况讨论，注意，else中的是计算子区间内的收益，
# 若遇到更大的收益会更新，因为为了防止多减去fee，因此prices[i]需要减fee
def maxProfit(prices, fee):
    minPrice = prices[0]
    total = 0
    for i in range(1, len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] < minPrice + fee:
            continue
        else:
            total += prices[i] - minPrice - fee
            minPrice = prices[i] - fee
    return total

print(maxProfit(prices, fee))