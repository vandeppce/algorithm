# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

# 由于要求min的复杂度为o(1)，因此min()方法不可行。
# 使用一个辅助栈记录截止到每个元素时的最小值。
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            if x < self.minStack[-1]:
                self.minStack.append(x)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minStack[-1]
