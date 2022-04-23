# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
s = "{[]}"
s = "{}]"
s = "{}["
def isValid(s):
    stack = []
    for chr in s:
        if chr == "(" or chr == "{" or chr == "[":
            stack.append(chr)
        elif chr == ")":
            if not stack:
                return False
            if stack.pop() != "(":
                return False
        elif chr == "}":
            if not stack:
                return False
            if stack.pop() != "{":
                return False
        else:
            if not stack:
                return False
            if stack.pop() != "[":
                return False
    if not stack:
        return True
    else:
        return False

print(isValid(s))

"""
# 二刷
def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            else:
                if len(stack) == 0 or stack.pop() != c:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
"""