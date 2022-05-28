# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
# 同时保持非零元素的相对顺序。

nums = [0,1,0,3,12]
nums = [0]
nums = [1,2,3]
def moveZeroes(nums):
    length = len(nums)
    slow = 0
    fast = 0

    while fast < length:
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        else:
            fast += 1

    while slow < fast:
        nums[slow] = 0
        slow += 1

    return nums

print(moveZeroes(nums))