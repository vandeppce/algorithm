# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
# 单调队列（递减）
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        stack = []
        # 初始化栈
        for i in range(k):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
        res = [stack[0]]
        for i in range(k, len(nums)):
            if stack[0] == nums[i - k]:
                stack.pop(0)
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
            res.append(stack[0])
        return res