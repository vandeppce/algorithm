# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
#
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
#
# 以这种方式修改数组后，返回数组 可能的最大和 。
#
nums = [4, 2, 3]
k = 1
nums = [3,-1,0,2]
k = 3
nums = [2,-3,-1,5,-4]
k = 2

# 每次修改最小的数
def largestSumAfterKNegations(nums, k):
    nums = sorted(nums)
    while k:
        k -= 1
        nums[0] = -nums[0]
        nums = sorted(nums)
    return sum(nums)

"""
# 二刷，按绝对值排序，先修改所有负数。修改完了如果k还大于0，则反复修改最小的数
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key = lambda item: abs(item))
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            if k <= 0:
                return sum(nums)
        
        while k > 0:
            nums[0] = -nums[0]
            k -= 1
        return sum(nums)
"""
print(largestSumAfterKNegations(nums, k))