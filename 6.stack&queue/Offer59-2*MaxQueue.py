# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
#
# 若队列为空，pop_front 和 max_value 需要返回 -1
#

# queue存储队列，maxQueue为单调递减队列，用法同239。其实本质上是个滑动窗口问题。注意区分和Offer30的区别，后者为最小栈，pop是从最后一个元素开始，
# 因此不涉及到pop后整个队列的最大值变化

class MaxQueue:

    def __init__(self):
        self.queue = []
        self.maxQueue = []

    def max_value(self) -> int:
        if self.maxQueue:
            return self.maxQueue[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.maxQueue and self.maxQueue[-1] < value:
            self.maxQueue.pop()
        self.maxQueue.append(value)

    def pop_front(self) -> int:
        if not self.maxQueue and not self.queue:
            return -1
        else:
            ret = self.queue.pop(0)
            if ret == self.maxQueue[0]:
                self.maxQueue.pop(0)
            return ret


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()