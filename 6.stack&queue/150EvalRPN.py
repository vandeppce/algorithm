# 根据 逆波兰表示法，求表达式的值。
#
# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
# 注意 两个整数之间的除法只保留整数部分。
#
# 可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
#

tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPN(tokens):
    stack = []
    operations = ["+", "-", "*", "/"]

    for token in tokens:
        if token in operations:
            number1 = int(stack.pop())
            number2 = int(stack.pop())

            if token == "+":
                res = number1 + number2
            elif token == "-":
                res = number2 - number1
            elif token == "*":
                res = number1 * number2
            else:
                res = int(number2 / number1)
            stack.append(str(res))
        else:
            stack.append(token)
    return int(stack.pop())

print(evalRPN(tokens))