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

"""
# 二刷，直接判断当前值是否大于self.path的最后一个元素
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    
    def 8.backtracking(self, nums, start):
        if len(self.path) > 1:
            self.res.append(self.path[:])
        if start >= len(nums):
            return
        used_list = []
        for i in range(start, len(nums)):
            if nums[i] in used_list:
                continue
            else:
                used_list.append(nums[i])

                if len(self.path) == 0:
                    self.path.append(nums[i])
                    self.8.backtracking(nums, i + 1)
                    self.path.pop()
                else:
                    if nums[i] >= self.path[-1]:
                        self.path.append(nums[i])
                        self.8.backtracking(nums, i + 1)
                        self.path.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.8.backtracking(nums, 0)
        return self.res

# 另一种写法
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
        本题求自增子序列，所以不能改变原数组顺序
        '''
        self.8.backtracking(nums, 0)
        return self.paths

    def 8.backtracking(self, nums: List[int], start_index: int):
        # 收集结果，同78.子集，仍要置于终止条件之前
        if len(self.path) >= 2:
            # 本题要求所有的节点
            self.paths.append(self.path[:])
        
        # Base Case（可忽略）
        if start_index == len(nums):
            return

        # 单层递归逻辑
        # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        usage_list = set()
        # 同层横向遍历
        for i in range(start_index, len(nums)):
            # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
            if (self.path and nums[i] < self.path[-1]) or nums[i] in usage_list:
                continue
            usage_list.add(nums[i])
            self.path.append(nums[i])
            self.8.backtracking(nums, i+1)
            self.path.pop() 
"""
nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]
solu = Solution()
print(solu.findSubsequences(nums))