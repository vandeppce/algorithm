# 快速排序
# 原理：分而治之。快速排序应该算是在冒泡排序基础上的递归分治法。
#
# 在待排序的元素随机取一个元素，称为 "基准"（pivot）;
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
# 在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

# 在每一轮中，pivot先设置为最左边元素，从right往前查找，当遇到nums[right]<pivot，令nums[left]=nums[right]
# 随后left向右查找，当遇到nums[left]>pivot，令nums[right]=nums[left]
# 时间复杂度：nlogn；空间复杂度：logn；稳定性：不稳定
import random
nums = [49, 38, 65, 97, 76, 13, 27, 49]
# nums = [2]
nums = [3,2,1,5,6,4]
# partition1，选择pivot为最左侧元素，先右后左
def partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left

# partition2，选择pivot为随机元素，先左后右
"""
def partition2(nums, left, right):
    pivot = random.randint(left, right)
    nums[pivot], nums[right] = nums[right], nums[pivot]
    pivot = right
    right -= 1
    while left < right:
        while left < right and nums[left] <= nums[pivot]:
            left += 1
        while left < right and nums[right] >= nums[pivot]:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
    nums[left], nums[pivot] = nums[pivot], nums[left]
    return left
"""

def partition2(nums, l, r):
    # leetcode提交这个partition函数不会超时
    pivot = random.randint(l, r)
    nums[pivot], nums[r] = nums[r], nums[pivot]
    i = l - 1
    for j in range(l, r):
        if nums[j] < nums[r]:
            # 也就是说，这里的i记录的是>pivot的数值的前一位，当遇见小于pivot的数值时，i后移一位，进行交换
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i

def quickSort(nums, left, right):
    if left >= right:
        return nums # 这里返回值不可少

    partitionIdx = partition2(nums, left, right)
    quickSort(nums, left, partitionIdx - 1)
    quickSort(nums, partitionIdx + 1, right)

    return nums

print(quickSort(nums, 0, len(nums) - 1))