nums = [1,-2,-5,-4,-3,3,3,5]
target = -11

def fourSum(nums, target):
    nums = sorted(nums)
    res = []

    for i in range(len(nums)):
        if nums[i] >= 0 and nums[i] > target:
            break
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] >= 0 and nums[i] + nums[j] > target:
                break
            if j > i + 1 and nums[j - 1] == nums[j]:
                continue

            left = j + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

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