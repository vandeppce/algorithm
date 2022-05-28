# 在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。
#
# 现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：
#
#  nums1[i] == nums2[j]
# 且绘制的直线不与任何其他连线（非水平线）相交。
# 请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
#
# 以这种方法绘制线条，并返回可以绘制的最大连线数。
#

nums1 = [1,4,2]
nums2 = [1,2,4]
nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]
nums1 = [1,3,7,1,7,5]
nums2 = [1,9,2,5,1]

# 每次遍历设置dict字典记录nums2中数字使用情况
def maxUncrossedLines(nums1, nums2):
    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    numDic = {}
    for num in nums2:
        numDic[num] = numDic.get(num, 0) + 1

    for i in range(1, len(nums1) + 1):
        dic = numDic.copy()
        for j in range(1, len(nums2) + 1):
            if nums1[i - 1] == nums2[j - 1]:
                if dic[nums1[i - 1]] > 0:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

# 当然，也可以不用记录数字使用情况，直接是最长公共子序列的解法，和1143完全一样
def maxUncrossedLines(nums1, nums2):
    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    for i in range(1, len(nums1) + 1):
        for j in range(1, len(nums2) + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
print(maxUncrossedLines(nums1, nums2))