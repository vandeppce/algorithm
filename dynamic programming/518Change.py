# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
#
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
#
# 假设每一种面额的硬币有无限个。 
#
# 题目数据保证结果符合 32 位带符号整数。
#

# 外层for循环遍历物品（钱币），内层for遍历背包（金钱总额），此时是组合数
# 外层for循环遍历背包（金钱总额），内层for遍历物品（钱币），此时是排列数
amount = 5
coins = [1, 2, 5]

def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], amount + 1):
            dp[j] += dp[j - coins[i]]
    return dp[-1]

print(change(amount, coins))