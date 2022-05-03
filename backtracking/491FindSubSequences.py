# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
#
# 数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
#

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def isIncreasing(self, path):
        if len(path) <= 1:
            return False
        else:
            for i in range(1, len(path)):
                if path[i] < path[i - 1]:
                    return False
            return True

    def backtracking(self, nums, start):
        if self.isIncreasing(self.path):
            self.res.append(self.path[:])

        if start >= len(nums):
            return

        # 每层递归使用一个usage集合记录元素是否被使用
        usage = set()
        for i in range(start, len(nums)):
            if nums[i] in usage:
                continue
            usage.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

    def findSubsequences(self, nums):
        self.backtracking(nums, 0)
        return self.res

nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]
solu = Solution()
print(solu.findSubsequences(nums))