nums = [1,2,3]

class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def backtracking(self, nums, length):
        if len(self.path) == length:
            self.res.append(self.path[:])
            return
        for i in range(len(nums)):
            self.path.append(nums[i])
            tmp = nums.pop(i)
            self.backtracking(nums, length)
            nums.insert(i, tmp)
            self.path.pop()
    def permute(self, nums):
        self.backtracking(nums, len(nums))
        return self.res

solu = Solution()
print(solu.permute(nums))