# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

class MyStack:

    def __init__(self):
        self.stack_in = []
        self.stack_bak = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        while len(self.stack_in) > 1:
            self.stack_bak.append(self.stack_in.pop(0))
        x = self.stack_in.pop(0)
        while len(self.stack_bak) != 0:
            self.stack_in.append(self.stack_bak.pop(0))
        return x

    def top(self) -> int:
        while len(self.stack_in) > 0:
            self.stack_bak.append(self.stack_in.pop(0))
        x = self.stack_bak[-1]
        while len(self.stack_bak) != 0:
            self.stack_in.append(self.stack_bak.pop(0))
        return x

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_bak


"""
class MyStack:

    def __init__(self):
        self.queue_in = []
        self.queue_bak = []

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        while len(self.queue_in) > 1:
            self.queue_bak.append(self.queue_in.pop(0))
        res = self.queue_in.pop()
        while self.queue_bak:
            self.queue_in.append(self.queue_bak.pop(0))
        return res 

    def top(self) -> int:
        while self.queue_in:
            self.queue_bak.append(self.queue_in.pop(0))
        res = self.queue_bak[-1]
        while self.queue_bak:
            self.queue_in.append(self.queue_bak.pop(0))
        return res

    def empty(self) -> bool:
        return not self.queue_in
"""
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()