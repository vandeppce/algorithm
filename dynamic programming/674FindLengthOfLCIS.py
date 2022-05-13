# 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
#
# 连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，
# 都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
#

nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
nums = [1,3,6,7,9,4,10,5,6]
nums = [4,10,4,3,8,9]
def findLengthOfLCIS(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
    print(dp)
    return max(dp)

print(findLengthOfLCIS(nums))