# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
#
# 注意 这个数列必须是 严格 递增的。

nums = [1,3,5,4,7,6,9,8]
nums = [2, 2, 2, 2, 2]
nums = [1,2,4,3,5,4,7,2]
nums = [1,2]
# dp数组用来记录长度，count数组用来记录dp[i]的个数
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]

        maxLength = max(dp)
        res = 0
        for i, c in enumerate(dp):
            if c == maxLength:
                res += count[i]
        return res

print(findNumberOfLIS(nums))