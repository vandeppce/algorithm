# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

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