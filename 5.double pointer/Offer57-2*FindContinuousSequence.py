# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#

target = 15
target = 9
target = 120
# 双指针，从中间开始，因为对于target来说，如果可以由多个连续数字组成，那么最大的那个一定不会超过其一半+1
def findContinuousSequence(target):
    res = []
    left = target // 2
    if left + left + 1 == target:
        res.append([left, left + 1])
    right = left
    total = right
    while left >= 0:
        if total == target:
            res.insert(0, list(range(left, right + 1)))
            total -= right
            right -= 1
        elif total < target:
            left -= 1
            total += left
        else:
            total -= right
            right -= 1
    return res

print(findContinuousSequence(target))
