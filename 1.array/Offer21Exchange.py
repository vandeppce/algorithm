# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

nums = [1,2,3,4]
# 双指针，从一端开始
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] % 2 == 0:
                fast += 1
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
        return nums
# 双指针，从两端开始
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums