# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 双指针
# 使用一个循环遍历数组，对于当前遍历位置，对其后的子数组使用双指针

nums = [-1,0,1,2,-1,-4]
nums = []
nums = [0]
nums = [-2,-1,-1,0,1,1,2]
# nums = [0, 0]

def threeSum(nums):
    nums = sorted(nums)
    length = len(nums)
    res = []

    for i in range(length):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        right = length - 1
        left = i + 1

        while left < right:
            count = nums[i] + nums[right] + nums[left]
            if count < 0:
                left += 1
            elif count > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
    return res

print(threeSum(nums))