# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
#

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        minLength = len(nums)
        if sum(nums) < target:
            return 0
        while right < len(nums):
            while right < len(nums) and total < target:
                total += nums[right]
                right += 1
            while left < right and total >= target:
                total -= nums[left]
                left += 1
            minLength = min(minLength, right - left + 1)
        return minLength