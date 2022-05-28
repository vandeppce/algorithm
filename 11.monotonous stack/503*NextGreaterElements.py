# 给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），
# 返回 nums 中每个元素的 下一个更大元素 。
#
# 数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，
# 这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。
#

nums = [1,2,1]
nums = [1,2,3,4,3]
nums = [4,3,2,3,1]
nums = [1]
# 最多走两遍nums，也可以把两个nums拼到一起，求下一个最大值
def nextGreaterElements(nums):
    res = [-1] * len(nums)
    if len(nums) <= 1:
        return res
    cnt = 1
    i = 1
    stack = [0]
    while True:
        if nums[i] <= nums[stack[-1]]:
            stack.append(i)
        else:
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)
        cnt += 1
        i = cnt % len(nums)
        if cnt == 2 * len(nums):
            break
    return res

"""
# 二刷，扩充nums为二倍
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
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
"""
print(nextGreaterElements(nums))