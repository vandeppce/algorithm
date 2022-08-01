# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#

nums1 = [1,3]
nums2 = [2]
# 但是这种方法的复杂度为o(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < m:
            nums.extend(nums1[i:])
        if j < n:
            nums.extend(nums2[j:])
        if (m + n) % 2 == 1:
            return nums[(m + n) // 2]
        else:
            return (nums[(m + n) // 2 - 1] + nums[(m + n) // 2]) / 2