# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

# 双栈
class MyQueue:

    def __init__(self):
        self.queue_in = []
        self.queue_out = []

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if len(self.queue_out) == 0:
            while self.queue_in:
                self.queue_out.append(self.queue_in.pop())
        return self.queue_out.pop()

    def peek(self) -> int:
        if not self.queue_out:
            while self.queue_in:
                self.queue_out.append(self.queue_in.pop())
        return self.queue_out[-1]

    def empty(self) -> bool:
        return not self.queue_in and not self.queue_out

"""
# 二刷，每次操作后清空out数组恢复in数组
class MyQueue:

    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, x: int) -> None:
        self.stackIn.append(x)

    def pop(self) -> int:
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop())
        popNum = self.stackOut.pop()
        while self.stackOut:
            self.stackIn.append(self.stackOut.pop())
        return popNum
    def peek(self) -> int:
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop())
        retNum = self.stackOut[-1]
        while self.stackOut:
            self.stackIn.append(self.stackOut.pop())
        return retNum

    def empty(self) -> bool:
        return not self.stackIn and not self.stackOut
"""
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def push(self, x: int) -> None:
        self.stack_in.append(x)
    def pop(self) -> int:
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        res = self.stack_out.pop()
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())
        return res
    def peek(self) -> int:
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        res = self.stack_out[-1]
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())
        return res
    def empty(self) -> bool:
        return not self.stack_in
"""