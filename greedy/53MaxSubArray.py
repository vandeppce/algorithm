# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    maxArray = nums
    for i in range(1, len(nums)):
        if maxArray[i - 1] > 0:
            maxArray[i] = maxArray[i - 1] + nums[i]
    return max(maxArray)

print(maxSubArray(nums))