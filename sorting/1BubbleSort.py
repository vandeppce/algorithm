# 冒泡排序
# 它重复地访问要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# “冒泡”顾名思义，大元素会经由交换像一个泡泡一样慢慢"浮"到数列的顶端（升序排列）。

# 时间复杂度，n^2；空间复杂度，1；稳定性：稳定
nums = [3,6,4,2,11,10,5]

# 原始冒泡
def bubbleSort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# 改进冒泡，一次排序中都没有交换，则代表已经排好序，以后则不需要再排序了
def bubbleSort1(nums):
    for i in range(len(nums) - 1, 0, -1):
        flag = 0
        for j in range(i):
            if nums[j] > nums[j + 1]:
                flag = 1
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if not flag:
            return nums

print(bubbleSort(nums))
print(bubbleSort1(nums))