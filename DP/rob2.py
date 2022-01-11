# 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

nums = [1, 2, 3, 1]
nums = [1, 3, 3, 1, 4, 5, 7, 9]
nums = [0, 3, 2, 0]
length = len(nums)
if length <= 3:
    print(max(nums))

# 如果第二间的数额大于1+3，则说明后面所有的房间都不会考虑1和3，例如，2>1+3，那么第4间时，比较1，2，选择2。第5间时，比较2，3，选择2。第6间时，比较3，4，选择4。
# 反之，则说明后面所有的房间都有可能考虑1和2。则分两种情况讨论，选择1时，序列为1-length-1，选择2时，序列为2-length，选择较大值即可

if nums[1] > nums[2] + nums[0]:
    count = [0] * length
    count[0] = nums[0]
    count[1] = nums[1]
    count[2] = max(nums[0] + nums[2], nums[2])
    for i in range(3, length):
        count[i] = nums[i] + max(count[i - 2], count[i - 3])
    print(max(count))
else:
    count1 = [0] * (length - 1)
    count1[0] = nums[0]
    count1[1] = nums[1]
    count1[2] = max(nums[0] + nums[2], nums[2])
    for i in range(3, length - 1):
        count1[i] = nums[i] + max(count1[i - 2], count1[i - 3])
    ans1 = max(count1)

    count2 = [0] * (length - 1)
    count2[0] = nums[1]
    count2[1] = nums[2]
    count2[2] = max(nums[1] + nums[3], nums[3])
    for i in range(4, length):
        count2[i - 1] = nums[i] + max(count2[i - 3], count2[i - 4])
    ans2 = max(count2)

    print(max(ans1, ans2))