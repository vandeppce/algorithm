# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
#

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

# 从pop看push。遍历pop数组，对于每一个元素，查看其在pushed中所在的位置，当其小于上一个元素弹出的位置减一时，说明跨过了元素，无法弹出。
# 例如，对于[1,2,3,4,5]，[4,3,5,1,2]。首先弹出4，其在push中的位置是3，可以弹出，将弹出push 3。然后弹出3，3在push中的位置为2，说明弹出4后接着弹出3。
# 然后弹出5，5在push中的位置变为2，说明先push 5 又pop5，有效。然后弹出1，而1在push中的位置是0，2-0=2，说明中间跨过了位置为1的元素，也就是2，无法弹出。
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        prev = 0
        for num in popped:
            idx = pushed.index(num)
            if idx >= prev - 1:
                pushed.pop(idx)
                prev = idx
            else:
                return False
        return True

# 另一种做法。使用辅助栈，循环压入push中的元素，当栈顶元素等于pop[i]时，出栈。如果最后stack为空，说明有效
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack