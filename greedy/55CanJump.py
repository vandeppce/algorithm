# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标。
#

# 在每一步时，判断下一步能到达的最远位置，然后跳跃至可以使得下一步达到最远的那个位置

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [1, 2, 3]
nums = [1, 1, 1, 0]
def canJump(nums) -> bool:
    if len(nums) == 1:
        return True

    i = 0
    while i < len(nums):
        currJump = nums[i]
        steps = 0
        nextId = i
        for j in range(currJump + 1):
            if i + j + nums[i + j] >= len(nums) - 1:
                return True
            if j + nums[i + j] > steps:
                steps = j + nums[i + j]
                nextId = i + j
        if i == nextId:
            return False
        i = nextId
    return False

"""
# 二刷
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        while i < len(nums):
            maxSteps = nums[i] + 1
            fastDis = 0
            for step in range(maxSteps):
                nextDis = step + nums[i + step]
                if i + nextDis >= len(nums) - 1:
                    return True
                elif nextDis >= fastDis:
                    fastDis = nextDis
                    nextStep = i + step
                if nextDis == 0:
                    return False
            i = nextStep
        return True
"""
print(canJump(nums))