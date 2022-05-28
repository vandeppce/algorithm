# 归并排序
# 原理：分而治之。
# 分（divide）：将一个序列从中间分成两部分，这两部分再二分下去，直到所有子序列长度为1不能再分。
# 治（conquer）：用一个新的序列将两部分排好序的子序列合并在一起，使得这个新序列也有序。
# 我们可以开辟一个临时数组来辅助我们的归并
# 时间复杂度：nlogn；空间复杂度1；稳定性：稳定
nums = [14, 2, 34, 43, 21, 19]

def merge(left, right):
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i == len(left):
        res.extend(right[j:])
    else:
        res.extend(left[i:])
    return res

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left, right)

print(mergeSort(nums))