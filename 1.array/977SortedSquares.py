# 给你一个按 非递减顺序 排序的整数数组 nums，
# 返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

# 双指针
nums = [-4,-1,0,3,10]
nums = [-7,-3,2,3,11]
left = 0
right = len(nums) - 1

res = []
while left <= right:
    if nums[left] * nums[left] >= nums[right] * nums[right]:
        res.insert(0, nums[left] ** 2)
        left += 1
    else:
        res.insert(0, nums[right] ** 2)
        right -= 1

print(res)