# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]

def fourSumCount(nums1, nums2, nums3, nums4):
    countTable = {}
    n = len(nums1)
    count = 0

    for i in range(n):
        for j in range(n):
            if 0 - (nums1[i] + nums2[j]) not in countTable.keys():
                countTable[0 - nums1[i] - nums2[j]] = 1
            else:
                countTable[0 - nums1[i] - nums2[j]] += 1

    for i in range(n):
        for j in range(n):
            query = nums3[i] + nums4[j]
            if query in countTable.keys():
                count += countTable[query]

    return count

print(fourSumCount(nums1, nums2, nums3, nums4))