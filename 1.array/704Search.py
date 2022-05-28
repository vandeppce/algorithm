# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
# 二分查找

nums = [-1, 0, 3, 5, 9, 12]
target = 9
# nums = [-1,0,3,5,9,12]
# target = 2

def search(nums, target):
    length = len(nums)
    left = 0
    right = length - 1

    while right >= left:
        middle = (left + right) // 2
        middle_num = nums[middle]
        if middle_num == target:
            return middle
        elif middle_num < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

print(search(nums, target))