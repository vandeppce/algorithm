# 给你一个整数数组 nums ，请计算数组的 中心下标 。
#
# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
#
# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
#
# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
#

nums = [1, 7, 3, 6, 5, 6]
nums = [1, 2, 3]
nums = [2, 1, -1]
def pivotIndex(nums):
    for i in range(len(nums)):
        left = sum(nums[:i])
        right = sum(nums[i + 1:])
        if left == right:
            return i
    return -1

# 另一种
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1
print(pivotIndex(nums))

