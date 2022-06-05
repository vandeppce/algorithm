# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，
# 可以看成任意数字。A 不能视为 14。
#

# 排序，然后从非0数开始记，不能有相同的非零数，并且最大值减非0最小值小于等于4，这样缺失部分可以用0填上
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        left = 0
        while left < 5 and nums[left] == 0:
            left += 1
        for i in range(left + 1, 5):
            if nums[i] == nums[i - 1]:
                return False
        return nums[-1] - nums[left] <= 4