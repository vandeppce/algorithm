# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

# 如果只有一个，那么可以直接异或遍历
"""
def singleNumber(self, nums: List[int]) -> List[int]:
    x = 0
    for num in nums:  # 1. 遍历 nums 执行异或运算
        x ^= num
    return x;         # 2. 返回出现一次的数字 x
"""

nums = [1,2,5,2]
# 1. 首先遍历nums执行异或，得到的结果是x异或y
# 2. 循环左移m
# 根据异或运算的定义，如果x^y某二进制位为1，则x和y的此二进制位一定不同。换言之，找到x^y为1的二进制为，就可以将nums拆分成两个数组，分别执行异或遍历即得到x和y
# 根据与运算的特点，可知对于任意整数a有
# 若a&0001=1，则a的第一位为1
# 若a&0010=1，则a的第二位为1
# 3. 拆分成两个数组，分别遍历异或

def singleNumbers(nums):
    n = 0
    m = 1
    x = 0
    y = 0
    # 1 循环异或nums，得到x^y
    for num in nums:
        n = n ^ num
    # 2 循环左移m，得到n的第一个为1的二进制位
    while n & m == 0:
        m = m << 1
    # 3 对nums进行分组，分别执行异或，此时x和y落入了两个组，并且两个组里的其他数都是成对出现
    for num in nums:
        if num & m == 0:
            x = x ^ num
        else:
            y = y ^ num
    return [x, y]

"""
# 二刷
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 得到x^y
        n = 0
        for num in nums:
            n ^= num
        # 计算x与y哪一位不相等
        m = 1
        while n & m == 0:
            m <<= 1
        # 分组，此时x和y分别落入两个组
        g1 = []
        g2 = []
        for num in nums:
            if num & m:
                g1.append(num)
            else:
                g2.append(num)
        # 每个组计算
        n1, n2 = 0, 0
        while g1 or g2:
            if g1:
                n1 ^= g1.pop()
            if g2:
                n2 ^= g2.pop()
        return [n1, n2]
"""
print(singleNumbers(nums))