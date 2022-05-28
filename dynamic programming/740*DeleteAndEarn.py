# 给你一个整数数组 nums ，你可以对它进行一些操作。
#
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。
#
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
#

# dp[i]表示截止到数字i，可以获得的最大点数。所以有选择i和不选i两种，不选i的话就是dp[i-1]，选择的话就是dp[i-2]+dp[i]
nums = [2,2,3,3,3,4,5,5,6,6,6,7,9]

def deleteAndEarn(nums):
    nums = sorted(nums)
    dp = [0] * (max(nums) + 1)
    for num in nums:
        dp[num] += num
    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 2] + dp[i], dp[i - 1])
    print(dp)

print(deleteAndEarn(nums))