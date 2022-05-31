# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。

nums = [-2,1,-3,4,-1,2,1,-5,4]
# 贪心算法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums.copy()
        maxNum.insert(0, 0)
        for i in range(len(nums)):
            if maxNum[i] > 0:
                maxNum[i + 1] = maxNum[i] + nums[i]
        return max(maxNum[1:])

# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)