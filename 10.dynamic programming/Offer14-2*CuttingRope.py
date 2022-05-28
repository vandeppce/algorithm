# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
# 每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 动态规划
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], (j * (i - j)), (dp[j] * (i - j))) # 注意，不能在这里取模，因为取模以后大小就变了，不能用来比较max
        return dp[-1] % 1000000007

# 贪心算法，取更多的3，如果最后是4那么拆成两个2
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        total = 1
        while n > 4:
            total *= 3
            n -= 3
        if n == 4:
            total = total * 2 * 2
        else:
            total = total * n
        return total % 1000000007