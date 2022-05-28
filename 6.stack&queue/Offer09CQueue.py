# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。
# (若队列中没有元素，deleteHead 操作返回 -1 )
#
#

class CQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        if not self.inStack:
            return -1
        while self.inStack:
            self.outStack.append(self.inStack.pop())
        ret = self.outStack.pop(-1)
        while self.outStack:
            self.inStack.append(self.outStack.pop())
        return ret


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()