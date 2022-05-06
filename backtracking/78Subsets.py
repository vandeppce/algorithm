# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

# 注意区分和前面切分问题的区别，切分是连续序列，子集不是
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracking(self, nums, start):
        self.res.append(self.path[:])
        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

    def subsets(self, nums):
        self.backtracking(nums, 0)
        return self.res

nums = [1, 2, 3]
solu = Solution()
print(solu.subsets(nums))