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


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()