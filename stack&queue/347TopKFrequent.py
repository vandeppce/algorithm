# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

# 小顶堆

import heapq
nums = [1,1,1,2,2,3]
k = 2

def topKFrequent(nums, k):
    frequencyTable = {}
    for num in nums:
        frequencyTable[num] = frequencyTable.get(num, 0) + 1

    # 对频率排序
    heap = []
    for key, value in frequencyTable.items():
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for i in range(k): # 此时输出为前k个频率从小到大排序
        res.append(heapq.heappop(heap)[1])
    return res

print(topKFrequent(nums, k))