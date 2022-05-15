# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
'''
# 动规，记录左右最大值
def trap(height):
    maxLeft = [0]
    maxRight = [0]
    res = 0
    for i in range(1, len(height)):
        maxLeft.append(max(maxLeft[i - 1], height[i - 1]))
    print(maxLeft)
    for i in range(len(height) - 2, -1, -1):
        maxRight.insert(0, max(maxRight[0], height[i + 1]))
    print(maxRight)
    for i in range(len(height)):
        res += max(0, min(maxLeft[i], maxRight[i]) - height[i])

    return res
'''

# 单调栈，递减
def trap(height):
    res = 0
    stack = [[0, height[0]]]
    for i in range(1, len(height)):
        if height[i] < stack[-1][1]:
            stack.append([i, height[i]])
        elif height[i] == stack[-1][1]:
            stack[-1] = [i, height[i]]
        else:
            while stack and height[i] > stack[-1][1]:
                mid = stack.pop()[1]
                if stack:
                    left = stack[-1][1]
                    right = height[i]
                    res += (min(left, right) - mid) * (i - stack[-1][0] - 1)
            stack.append([i, height[i]])
    return res
print(trap(height))