# 是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
# 这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
'''
# 通过记录含有首位的标志位，这样做不对
def rob(nums):
    containFirst = [0] * len(nums)
    dp = [0] * len(nums)
    containFirst[0] = 1
    dp[0] = nums[0]
    if nums[0] > nums[1]:
        dp[1] = nums[0]
        containFirst[1] = 1
    else:
        dp[1] = nums[1]

    if len(nums) == 2:
        return dp[1]
    else:
        for i in range(2, len(nums) - 1):
            temp1 = dp[i - 2] + nums[i]
            temp2 = dp[i - 1]

            if temp1 > temp2:
                dp[i] = temp1
                containFirst[i] = containFirst[i - 2]
            else:
                dp[i] = temp2
                containFirst[i] = containFirst[i - 1]

        last = len(nums) - 1
        if containFirst[last - 2] == 1 and containFirst[last - 1] == 1:
            dp[last] = max(nums[last], dp[last - 1])
        elif containFirst[last - 2] == 0 and containFirst[last - 1] == 1:
            dp[last] = max(dp[last - 2] + nums[last], dp[last - 1])
        elif containFirst[last - 2] == 1 and containFirst[last - 1] == 0:
            dp[last] = max(nums[last], dp[last - 1])
        else:
            dp[last] = max(dp[last - 2] + nums[last], dp[last - 1])
        print(dp)
        return dp[last]
'''
# 三种情况，不偷第一间和最后一间；偷第一间不偷最后一间；偷最后一间不偷第一间。后两种情况包含第一种
class Solution:
    def implement(self, nums):
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        robFirst = self.implement(nums[:-1])
        robLast = self.implement(nums[1:])
        # 两者取较大值即可
        return max(robFirst, robLast)
nums = [2,3,2]
nums = [1,2,3,1]
nums = [1,2,3]
# nums = [2,1,3,9,7]
nums = [0]
nums = [1,1]
nums = [1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]
print(rob(nums))