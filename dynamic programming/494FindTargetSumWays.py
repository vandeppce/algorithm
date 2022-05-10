# 给你一个整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
# L + R = S, L - R = target. 注意这个问题是组合问题，而前面的01背包问题都是装填最大值
nums = [1,1,1,1,1]
target = 3

def findTargetSumWays(nums, target):
    if sum(nums) < abs(target) or (sum(nums) + target) % 2 == 1:
        return 0
    bag_size = (sum(nums) + target) // 2
    dp = [0] * (bag_size + 1)
    dp[0] = 1
    for i in range(len(nums)):
        for j in range(bag_size, nums[i] - 1, -1):
            dp[j] += dp[j - nums[i]]
    return dp[-1]

print(findTargetSumWays(nums, target))