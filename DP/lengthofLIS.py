# 最长上升子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#

nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
nums = [1,3,5,4,7]

length = len(nums)
lengthLIS = [1] * length

for i in range(length):
    tmp = 1
    for j in range(i):
        if nums[i] > nums[j]:
            tmp = max(tmp, lengthLIS[j] + 1)
    lengthLIS[i] = tmp
print(lengthLIS)