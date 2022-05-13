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

print(findLength(nums1, nums2))
