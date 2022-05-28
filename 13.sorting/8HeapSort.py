# 堆排序
# https://zhuanlan.zhihu.com/p/350053229
# https://blog.csdn.net/weixin_44480914/article/details/112321825
# 先用给定数组构建完全二叉树，然后从下向上遍历构造大顶堆
# 利用大顶堆进行排序。首先将根节点和最底层最右侧元素交换，即把最大值交换到最后，然后再构造大顶堆，循环操作
# 时间复杂度：nlogn；空间复杂度：1；稳定性：不稳定

s1 = [49, 38, 65, 97, 76, 13, 27, 49, 10]
def down(s, node, end):  # s是列表，node是父节点，end是列表长度
    """从上面到下面判断是否符合大顶堆，不符合就交换"""
    root = node  # 父节点
    child = 2 * root + 1  # 子节点
    while child < end:
        if s[child] < s[child + 1] and (child + 1) < end:  # 找出较大的子节点
            child += 1
        if s[child] > s[root]:  # 如果子节点大于父节点，交换
            s[child], s[root] = s[root], s[child]
            root = child
        child = child * 2 + 1

def buildHeap(s, size):
    """从倒数第二排的非叶子节点开始创建大顶堆"""
    for i in range(size // 2 - 1, -1, -1):
        down(s, i, size)

def heapSort(s, size):
    buildHeap(s, size)
    for i in range(size - 1, 0, -1):
        s[0], s[i] = s[i], s[0]
        down(s, 0, i)

heapSort(s1, len(s1))
print(s1)