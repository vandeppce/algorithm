# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
intervals = [[1,4],[2,3]]

# 排序，从小到大合并。每次只和res数组中的最后一个比较交叉程度即可
def merge(intervals):
    intervals = sorted(intervals)
    res = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= res[-1][1]:
            res[-1] = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]
        else:
            res.append(interval)
    return res

print(merge(intervals))