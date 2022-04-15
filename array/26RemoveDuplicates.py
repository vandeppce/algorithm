# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
# 返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。

nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1, 1, 2]
nums = [1, 2]
def removeDuplicate(nums):
    length = len(nums)
    slow = 0
    fast = 0

    while fast < length:
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1

    return slow + 1, nums

print(removeDuplicate(nums))