# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

nums = [3, 4, 3, 3]

# 排序
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # 第一种情况，开始
        if nums[0] != nums[1]:
            return nums[0]
        # 第二种情况，末尾
        elif nums[-1] != nums[-2]:
            return nums[-1]
        # 第三种情况，中间
        else:
            for i in range(3, len(nums) - 3):
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]