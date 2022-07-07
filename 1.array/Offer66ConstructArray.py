# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
# 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
#

a = [1,2,3,4,5]
'''
# 超时
def constructArr(a):
    pre = 1
    res = []
    for i in range(len(a)):
        back = 1
        for j in range(i + 1, len(a)):
            back *= a[j]
        res.append(pre * back)
        pre *= a[i]
    return res
'''

# 先左后右
def constructArr(a):
    if not a:
        return a
    tmp = 1
    res = [1]
    for i in range(1, len(a)):
        tmp *= a[i - 1]
        res.append(tmp)
    tmp = 1
    for j in range(len(a) - 2, -1, -1):
        tmp *= a[j + 1]
        res[j] *= tmp
    return res
print(constructArr(a))