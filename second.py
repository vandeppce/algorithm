nums = [1,2,1]

class Solution:
    def nextGreaterElements(self, nums):
        length = len(nums)
        res = [-1] * length * 2
        nums.extend(nums)
        stack = [[0, nums[0]]]
        for i in range(1, len(nums)):
            while stack and nums[i] > stack[-1][1]:
                idx = stack.pop()[0]
                res[idx] = nums[i]
            stack.append([i, nums[i]])
        return res[:length]

solu = Solution()
print(solu.nextGreaterElements(nums))