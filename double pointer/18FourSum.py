# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
#
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11

def fourSum(nums, target):
    length = len(nums)
    res = []
    nums = sorted(nums)

    for i in range(length):
        if nums[i] >= 0 and nums[i] > target:
            break
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        for j in range(i + 1, length):
            if nums[i] + nums[j] >= 0 and nums[i] + nums[j] > target:
                break
            if j > i + 1 and nums[j - 1] == nums[j]:
                continue

            left = j + 1
            right = length - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
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