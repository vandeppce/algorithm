# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

nums = [1,3,5,6]
target = 2

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

    return left, right

print(search(nums, target))