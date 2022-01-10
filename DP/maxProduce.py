# 乘积最大子组数
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

nums = [2, 3, -2, 4]
# nums = [-2,0,-1]
# nums = [-3, -1, -1]
# nums = [-2, 3, -4]
length = len(nums)
pos = [0] * length
neg = [0] * length

pos[0] = nums[0]
neg[0] = nums[0]

for i in range(1, length):
    tmp = nums[i]

    pro1 = tmp * pos[i - 1]
    pro2 = tmp * neg[i - 1]

    if tmp >= 0:
        pos[i] = max(pro1, tmp)
        neg[i] = pro2
    else:
        pos[i] = pro2
        neg[i] = min(pro1, tmp)