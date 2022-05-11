# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#

n = 12
n = 13
n = 1
def numSquares(n):
    nums = []
    for i in range(1, n + 1):
        if i * i <= n:
            nums.append(i * i)
        else:
            break

    dp = [n + 1] * (n + 1)
    dp[0] = 0

    for i in range(len(nums)):
        for j in range(nums[i], n + 1):
            dp[j] = min(dp[j], dp[j - nums[i]] + 1)
    print(dp)
    return dp[-1]
print(numSquares(n))