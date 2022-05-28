# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
def findLength(nums1, nums2):
    dp = [[0] * len(nums2) for _ in range(len(nums1))]
    res = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > res:
                    res = dp[i][j]
    return res

"""
# 二刷，由于要求的是连续的数组，所以当遇到s[i]!=s[j]时，不需要进行操作，也就是说不需要将dp[i][j]置为前面的最大值
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        res = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > res:
                        res = dp[i][j]
        return res
"""
print(findLength(nums1, nums2))
