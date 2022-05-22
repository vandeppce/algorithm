# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
#
# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
# 右旋
# 反转整个字符串
# 反转区间为前k的子串
# 反转区间为k到末尾的子串

# 左旋
# 反转区间为前n的子串
# 反转区间为n到末尾的子串
# 反转整个字符串
nums = [-1,-100,3,99]
k = 2
nums = [1,2,3,4,5,6,7]
k = 1
class Solution:
    def rotate(self, A: List[int], k: int) -> None:
        def reverse(i, j):
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        n = len(A)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)