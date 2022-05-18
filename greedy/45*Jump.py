# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 假设你总是可以到达数组的最后一个位置。
#
# 思路同55
nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
def jump(nums):
    if len(nums) == 1:
        return 0

    jumps = 0
    i = 0
    while i < len(nums):
        currJump = nums[i]
        nextPos = 0
        nextId = i
        # 注意，这层判断要在循环外
        if i + currJump >= len(nums) - 1:
            return jumps + 1
        for j in range(currJump + 1):
            """ 这样写不对
            if i + j + nums[i + j] >= len(nums) - 1:
                return jumps + 2
            """
            if j + nums[i + j] > nextPos:
                nextPos = j + nums[i + j]
                nextId = i + j
        i = nextId
        jumps += 1
    return jumps

print(jump(nums))