# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
# 得到dp[j]（考虑coins[i]），只有一个来源，dp[j - coins[i]]（没有考虑coins[i]）。
# 凑足总额为j - coins[i]的最少个数为dp[j - coins[i]]，那么只需要加上一个钱币coins[i]即dp[j - coins[i]] + 1就是dp[j]（考虑coins[i]）
# 所以dp[j] 要取所有 dp[j - coins[i]] + 1 中最小的。
# 递推公式：dp[j] = min(dp[j - coins[i]] + 1, dp[j]);
# 完全背包问题
coins = [1, 2, 5]
amount = 11
coins = [2]
amount = 3
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化：总数为0，那么最少硬币个数是0，所以dp[0]=0。另外，由于dp是取最小值，所以应该初始化为一个很大的值
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        if dp[-1] > amount:
            return -1
        else:
            return dp[-1]

print(coinChange(coins, amount))