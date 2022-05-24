# 计数排序
# 计数排序先找到待排序列表中的最大值 k，开辟一个长度为 k+1 的计数列表，计数列表中的所有初始值都为 0。
# 走访待排序列表，如果走访到的元素值为 i，则计数列表中索引 i 的值加1，走访完整个待排序列表，就可以统计出待排序列表中每个值的数量。
# 然后创建一个新列表，根据计数列表中统计的数量，依次在新列表中添加对应数量的 i ，得到排好序的列表。
# 时间复杂度：n+k；空间复杂度：n+k；稳定性：稳定

nums = [5, 7, 3, 7, 2, 3, 2, 5, 9, 5, 7, 6]

def countingSort(nums):
    if len(nums) < 2:
        return nums
    maxNum = max(nums)
    count = [0] * (maxNum + 1)
    for num in nums:
        count[num] += 1
    res = []
    for i in range(len(count)):
        for j in range(count[i]):
            res.append(i)
    return res

print(countingSort(nums))