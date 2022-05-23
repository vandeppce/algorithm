# 插入排序
# 通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
#
# 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
# 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
# （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

# 时间复杂度：n^2；空间复杂度：1；稳定性：稳定
nums = [2, 1, 9, 11, 10, 8, 7]
def insertionSort(nums):
    for i in range(1, len(nums)):
        curr = nums[i]
        for j in range(i - 1, -1, -1): # 前i-1个元素已经按照升序
            if curr < nums[j]: # 说明找到curr要在前i-1个元素之间
                nums[j + 1] = nums[j]
                nums[j] = curr
            else: # 说明前j个元素都比curr小
                break
    return nums

print(insertionSort(nums))