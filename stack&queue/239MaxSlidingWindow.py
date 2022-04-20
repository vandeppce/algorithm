# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回 滑动窗口中的最大值 。

nums = [1,3,-1,-3,5,3,6,7]
k = 3

'''
# 暴力搜索 o(nxk)
def maxSlidingWindow(nums, k):
    res = []
    if len(nums) < k:
        return max(nums)
    else:
        left = 0
        right = k
        while right <= len(nums):
            res.append(max(nums[left: right]))
            left += 1
            right += 1
    return res
'''

# 单调递减队列
class myQueue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop(-1)
        self.queue.append(value)

    def pop(self, value):
        if self.queue[0] == value and self.queue:
            self.queue.pop(0)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = myQueue()
        res = []

        # 前k个
        for i in range(k):
            queue.push(nums[i])
        res.append(queue.front())

        for i in range(k, len(nums)):
            queue.pop(nums[i - k])
            queue.push(nums[i])
            res.append(queue.front())

        return res

print(maxSlidingWindow(nums, k))