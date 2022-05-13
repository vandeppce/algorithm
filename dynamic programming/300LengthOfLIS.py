# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#

nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
# nums = [4,10,4,3,8,9]
nums = [1,3,6,7,9,4,10,5,6]
"""
# 这样不对，只比较了前一个值
def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    return dp[-1]
"""

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # 返回dp的最大值
    return max(dp)
print(lengthOfLIS(nums))
