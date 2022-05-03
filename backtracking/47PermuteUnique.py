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