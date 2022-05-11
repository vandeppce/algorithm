# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
#
# 题目数据保证答案符合 32 位整数范围。
#

nums = [1,2,3]
target = 4

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    # 这样不对，这样没考虑顺序
    for i in range(len(nums)):
        for j in range(nums[i], target + 1):
            dp[j] += dp[j - nums[i]]
    print(dp)

    # 这样才对，考虑了顺序
    for j in range(target + 1):
        for i in range(len(nums)):
            if j >= nums[i]:
                dp[j] += dp[j - nums[i]]
    print(dp)

print(combinationSum4(nums, target))