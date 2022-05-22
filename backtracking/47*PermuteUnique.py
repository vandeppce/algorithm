# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 同层元素不能重复使用，所以使用usage数组
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracking(self, nums):
        if not nums:
            self.res.append(self.path[:])

        usage = set()
        for i in range(len(nums)):
            if nums[i] in usage:
                continue
            curr = nums.pop(i)
            usage.add(curr)
            self.path.append(curr)
            self.backtracking(nums)
            self.path.pop()
            nums.insert(i, curr)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums)
        return self.res

"""
#二刷，不实用usage数组，但是要对nums排序
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    
    def backtracking(self, nums):
        if not nums:
            self.res.append(self.path[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.path.append(nums[i])
            ret = nums.pop(i)
            self.backtracking(nums)
            self.path.pop()
            nums.insert(i, ret)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(sorted(nums))
        return self.res
"""

"""
# 三刷，差不多，used数组
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def backtracking(self, nums, length):
        if len(self.path) == length:
            self.res.append(self.path[:])
            return
        used = []
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            else:
                self.path.append(nums[i])
                tmp = nums.pop(i)
                self.backtracking(nums, length)
                nums.insert(i, tmp)
                self.path.pop()
                used.append(nums[i])
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(sorted(nums), len(nums))
        return self.res
"""