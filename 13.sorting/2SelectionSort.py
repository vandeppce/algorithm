# 选择排序
# 首先，从0–N-1范围内选择最大的数，交换到N-1位置；
# 然后，从0–N-2范围内选择最小的数，交换到N-2位置；
# 然后，从0–N-3范围内选择最小的数，交换到N-3位置；
# 重复上述过程
# 时间复杂度：n^2；空间复杂度：1；稳定性：不稳定
nums = [2, 1, 9, 11, 10, 8, 7]
def selectionSort(nums):
    for i in range(len(nums) - 1, 0, -1):
        maxIdx = i
        for j in range(i + 1):
            if nums[j] > nums[maxIdx]:
                maxIdx = j
        nums[maxIdx], nums[i] = nums[i], nums[maxIdx]
    return nums

print(selectionSort(nums))