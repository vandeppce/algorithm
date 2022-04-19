# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 双指针，分别在首尾，同时移动

s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
def reverseString(s):
    length = len(s)

    left = 0
    right = length - 1

    while left < right:
        sLeft = s[left]
        sRight = s[right]

        tmp = sLeft
        s[left] = sRight
        s[right] = tmp

        left += 1
        right -= 1

    return s

print(reverseString(s))