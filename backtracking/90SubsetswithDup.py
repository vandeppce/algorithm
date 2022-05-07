# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
# 去重，不使用used数组时需要先对nums排序，去重时要去除同行元素
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracking(self, nums, start):
        self.res.append(self.path[:])
        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(sorted(nums), 0)
        return self.res

nums = [1, 2, 2]
solu = Solution()
print(solu.subsetsWithDup(nums))