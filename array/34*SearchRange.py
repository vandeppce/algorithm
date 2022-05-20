# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#

nums = [5,7,7,8,10]
target = 8

def searchRange(nums, target):

    def getRightBorder(nums, target):
        left = 0
        right = len(nums) - 1
        rightBorder = -2

        while left <= right:
            middle = (left + right) // 2
            mid_num = nums[middle]
            if mid_num > target:
                right = middle - 1
            else:
                left = middle + 1
                rightBorder = left
        return rightBorder

    def getLeftBorder(nums, target):
        left = 0
        right = len(nums) - 1
        leftBorder = -2

        while left <= right:
            middle = (left + right) // 2
            mid_num = nums[middle]
            if mid_num >= target:
                right = middle - 1
                leftBorder = right
            else:
                left = middle + 1
        return leftBorder

    leftBorder = getLeftBorder(nums, target)
    rightBorder = getRightBorder(nums, target)

    if leftBorder == -2 or rightBorder == -2: return [-1, -1]
    if rightBorder -leftBorder >1: return [leftBorder + 1, rightBorder - 1]
    else: return [-1, -1]
    
print(searchRange(nums, target))

'''
# 二刷答案
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getLeftBorder(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                middle = (left + right) // 2
                mid_num = nums[middle]
                if mid_num >= target:
                    right = middle - 1
                else:
                    left = middle + 1
            return right

        def getRightBorder(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                middle = (left + right) // 2
                mid_num = nums[middle]
                if mid_num > target:
                    right = middle - 1
                else:
                    left = middle + 1
            return left

        leftBorder = getLeftBorder(nums, target)
        rightBorder = getRightBorder(nums, target)

        if rightBorder - leftBorder < 2:
            return [-1, -1]
        else:
            return [leftBorder + 1, rightBorder - 1]
'''

"""
# 三刷，注意二分边界条件，比前面的更好
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftBorder(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                mid_val = nums[mid]
                if mid_val >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def rightBorder(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                mid_val = nums[mid]
                if mid_val <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = leftBorder(nums, target)
        right = rightBorder(nums, target)
        if left > right:
            return [-1, -1]
        else:
            return [left, right]
"""