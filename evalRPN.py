# 根据 逆波兰表示法，求表达式的值。
#
# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

# 输入：tokens = ["2","1","+","3","*"]
# 输出：9
# 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = []

for item in tokens:
    if item != "+" and item != "-" and item != "*" and item != "/":
        stack.append(int(item))
    elif item == "+":
        item1 = stack.pop()
        item2 = stack.pop()

        res = item1 + item2
        stack.append(res)
    elif item == "-":
        item1 = stack.pop()
        item2 = stack.pop()

        res = item2 - item1
        stack.append(res)
    elif item == "*":
        item1 = stack.pop()
        item2 = stack.pop()

        res = item1 * item2
        stack.append(res)
    elif item == "/":
        item1 = stack.pop()
        item2 = stack.pop()

        res = int(item2 / item1)
        stack.append(res)
print(stack[0])