# 统计一个数字在排序数组中出现的次数。
# 二分查找，一种方式是分别计算左右端点，或者计算一侧端点然后继续遍历
nums = []
target = 8
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        count = 0
        while left <= right:
            mid = (left + right) // 2
            mid_value = nums[mid]
            if mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return count
        else:
            while left < len(nums) and nums[left] == target:
                count += 1
                left += 1
            return count

solu = Solution()
print(solu.search(nums, target))