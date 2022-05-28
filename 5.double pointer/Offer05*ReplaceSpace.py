# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

s = "We are happy."

# 双指针法
def replaceSpace(s):
    # 扩展
    count = 0
    length1 = len(s)
    for chr in s:
        if chr == " ":
            count += 1
    s = list(s)
    s.extend([" "] * count * 2)
    length2 = len(s)

    # 双指针移动
    left = length1 - 1
    right = length2 - 1

    while left != right:
        if s[left] != " ":
            s[right] = s[left]
            left -= 1
            right -= 1
        else:
            s[right - 2: right + 1] = "%20"
            left -= 1
            right -= 3
    return "".join(s)

print(replaceSpace(s))