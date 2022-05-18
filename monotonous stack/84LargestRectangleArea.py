# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

heights = [2,1,5,6,2,3]
# heights = [2,4]
# heights = [7,1,2,3,4,5,6,2,3,4,9,7,6,0,9]
# heights = [2,1,2]

'''
# 单调递增栈
def largestRectangleArea(heights):
    heights.insert(0, 0)
    heights.append(0)
    stack = [[0, 0]]
    result = 0

    for i in range(1, len(heights)):
        if heights[i] > stack[-1][1]:
            stack.append([i, heights[i]])
        elif heights[i] == stack[-1][1]:
            stack[-1] = [i, heights[i]]
        else:
            while stack and heights[i] < stack[-1][1]:
                mid = stack.pop()[1]
                if stack:
                    left = stack[-1][0]
                    right = i
                    result = max(result, mid * (right - left - 1))
            stack.append([i, heights[i]])
    return result
'''

# 动规，记录每个点左右第一个较小值的索引，对于每一个点，其能构成的最大面积为其高度乘以夹在两侧较小值索引中间的部分的宽度
class Solution:
    def largestRectangleArea(self, heights) -> int:
        minLeft = [-1]
        minRight = [0] * len(heights)
        minRight[-1] = len(heights)

        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                minLeft.append(i - 1)
            else:
                t = i - 1
                while t >= 0 and heights[t] >= heights[i]:
                    t = minLeft[t]
                minLeft.append(t)

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[i + 1]:
                minRight[i] = i + 1
            else:
                t = i + 1
                while t < len(heights) and heights[t] >= heights[i]:
                    t = minRight[t]
                minRight[i] = t
        print(minLeft)
        print(minRight)
        res = 0
        for i in range(len(heights)):
            print(heights[i] * (minRight[i] - minLeft[i] - 1))
            res = max(res, heights[i] * (minRight[i] - minLeft[i] - 1))
        return res

"""
# 二刷，动规
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftMin = [-1] * len(heights)
        for i in range(1, len(heights)):
            temp = i - 1
            while temp >= 0 and heights[temp] >= heights[i]:
                temp = leftMin[temp]
            leftMin[i] = temp
        print(leftMin)

        rightMin = [len(heights)] * len(heights)
        for i in range(len(heights) - 2, -1, -1):
            temp = i + 1
            while temp < len(heights) and heights[temp] >= heights[i]:
                temp = rightMin[temp]
            rightMin[i] = temp
        print(rightMin)

        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i] * (rightMin[i] - leftMin[i] - 1))
        return res

# 单调递增栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        stack = [[0, 0]]
        result = 0

        for i in range(1, len(heights)):
            if heights[i] > stack[-1][1]:
                stack.append([i, heights[i]])
            elif heights[i] == stack[-1][1]:
                stack[-1] = [i, heights[i]]
            else:
                while stack and stack[-1][1] > heights[i]:
                    temp = stack.pop()
                    h = temp[1]
                    if stack:
                        left = stack[-1][0]
                        right = i
                        result = max(result, h * (right - left - 1))
                stack.append([i, heights[i]])
        return result
"""
solu = Solution()
print(solu.largestRectangleArea(heights))