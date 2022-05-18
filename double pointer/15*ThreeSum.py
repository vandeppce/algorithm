# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#

# 终止条件很多，可以减少运算开销

nums = [-1,0,1,2,-1,-4]
nums = []
nums = [0]
def threeSum(nums):
    res = []
    nums = sorted(nums)
    i = 0

    for i in range(len(nums)):
        start = nums[i]
        if start > 0:
            break
        if nums[i - 1] == nums[i] and i > 0:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = start + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([start, nums[left], nums[right]])
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
    return res

print(threeSum(nums))