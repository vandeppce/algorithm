# 给你一个字符串 s ，颠倒字符串中 单词 的顺序。
#
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
#
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
#
s = "the  sky is blue"
s = "  hello world  "
s = "a good   example"
# 双指针法
def reverseWords(s):
    # 1. 移除多余空格
    left = 0
    right = len(s) - 1
    # 开头空格
    while s[left] == " ":
        left += 1
    # 结尾空格
    while s[right] == " ":
        right -= 1
    # 中间空格
    tmp = ""
    while left <= right:
        if s[left] != " ":
            tmp += s[left]
        else:
            if s[left - 1] != " ":
                tmp += s[left]
        left += 1
    tmp = list(tmp)

    # 2. 字符串反向
    left = 0
    right = len(tmp) - 1

    while left < right:
        sLeft = tmp[left]
        sRight = tmp[right]
        exchange = sLeft
        tmp[left] = sRight
        tmp[right] = exchange

        left += 1
        right -= 1

    # 3. 单词反向
    slow = 0
    fast = 0
    tmp.append(" ")
    while fast < len(tmp):
        if tmp[fast] == " ":
            tmp[slow: fast] = tmp[slow: fast][::-1]
            slow = fast + 1
            fast = slow
        fast += 1
    return "".join(tmp[:-1])

print(reverseWords(s))