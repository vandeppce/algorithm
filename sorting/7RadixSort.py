# 基数排序
# 取得数组中的最大数，并取得位数；
# 对数位较短的数前面补零；
# 分配，先从个位开始，根据位值(0-9)分别放到0~9号桶中;
# 收集，再将放置在0~9号桶中的数据按顺序放到数组中;
# 重复3~4过程，直到最高位，即可完成排序。
# 时间复杂度：n*k；空间复杂度：n+k；稳定性：稳定

nums = [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]

def radixSort(nums):
    n = len(str(max(nums))) # 记录最大值的位数
    for k in range(n): # n轮排序
        bucketList = [[] for _ in range(10)] #因为每一位数字都是0~9，故建立10个桶
        for num in nums:
            bucketList[num // (10 ** k) % 10].append(num) #按第k位放入到桶中
        nums = []
        for bucket in bucketList:
            for num in bucket:
                nums.append(num) # 按当前桶的顺序重排列表
    return nums

print(radixSort(nums))