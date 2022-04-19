# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
nums = [3,2,2,3]
val = 3

def removeElement(nums, val):
    length = len(nums)
    slow = 0
    fast = 0

    while fast < length:
        if nums[fast] == val:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    return slow

print(removeElement(nums, val))