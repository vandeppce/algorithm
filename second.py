nums = [3,6,4,2,11,10,5]
nums1 = [3,6,4,2,11,12,5]
# 冒泡排序
def bubbleSort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# 归并排序
def merge(left, right):
    tmp = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[i])
            j += 1

    if i < len(left):
        tmp.extend(left[i:])
    else:
        tmp.extend(right[j:])
    return tmp
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

# 快排
def partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        if left < right:
            nums[left] = nums[right]
            left += 1
        while left < right and nums[left] <= pivot:
            left += 1
        if left < right:
            nums[right] = nums[left]
            right -= 1
    nums[left] = pivot
    return left

def quickSort(nums, left, right):
    if left < right:
        partitionIdx = partition(nums, left, right)
        quickSort(nums, 0, partitionIdx - 1)
        quickSort(nums, partitionIdx + 1, right)

print(bubbleSort(nums))
print(mergeSort(nums))
quickSort(nums1, 0, len(nums1) - 1)
print(nums1)