# 最大子序和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
#  
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
nums = [1]
length = len(nums)

count = nums
# count的每一个位置记录包含该位置元素的连续子数组最大和
for i in range(1, length):
    pre_max = count[i - 1]
    if pre_max + nums[i] >= nums[i]:
        count[i] = pre_max + nums[i]
print(max(count))