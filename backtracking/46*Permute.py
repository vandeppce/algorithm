# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 排列和组合不一样
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracking(self, nums):
        if not nums:
            self.res.append(self.path[:])
            return

        for i in range(len(nums)):
            curr = nums.pop(i)
            self.path.append(curr)
            self.backtracking(nums)
            self.path.pop()
            nums.insert(i, curr)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums)
        return self.res

"""
#二刷，记录used情况
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    
    def backtracking(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in self.path:
                self.path.append(nums[i])
                self.backtracking(nums)
                self.path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums)
        return self.res
"""