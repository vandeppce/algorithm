# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
#
# 注意：如果对空文本输入退格字符，文本继续为空。
#

s = "ab#c"
t = "ad#c"

# s = "ab##"
# t = "c#d#"

# s = "a#c"
# t = "b"

# s = "a##c"
# t = "#a#c"

def backspaceCompare(s, t):
    def realStr(s):
        ret = list(s)
        length = len(s)
        slow = 0
        fast = 0

        while fast < length:
            if s[fast] != "#":
                ret[slow] = s[fast]
                slow += 1
                fast += 1
            else:
                slow = max(0, slow - 1)
                fast += 1
        return ret[:slow]

    realS = realStr(s)
    realT = realStr(t)
    print(realS, realT)
    return realS == realT

print(backspaceCompare(s, t))