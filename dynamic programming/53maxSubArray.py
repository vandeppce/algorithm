# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
nums = [5,4,-1,7,8]

# 只需要和前一个比较大小
# dp[i]只有两个方向可以推出来：

# dp[i - 1] + nums[i]，即：nums[i]加入当前连续子序列和
# nums[i]，即：从头开始计算当前连续子序列和

def maxSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    print(dp)
    return max(dp)

print(maxSubArray(nums))