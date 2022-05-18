# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] 
# （若两个四元组元素一一对应，则认为两个四元组重复）：
#

nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
nums = [-2,-1,-1,1,1,2,2]
target = 0
nums = [1,0,-1,0,-2,2]
target = 0
nums = [2,2,2,2,2]
target = 8
nums = [-1,0,1,2,-1,-4]
target = -1
def fourSum(nums, target):
    length = len(nums)
    nums = sorted(nums)
    res = []
    for i in range(length):
        if nums[i] >= 0 and nums[i] > target:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, length):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if nums[j] >= 0 and nums[i] + nums[j] > target:
                break

            twoSum = nums[i] + nums[j]
            left = j + 1
            right = length - 1

            while left < right:
                total = twoSum + nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1

    return res

print(fourSum(nums, target))
