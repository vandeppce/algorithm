# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。
#

# 先排序，从小到大遍历，遇到区间重叠的就把右端点较大的删掉（右端点大说明可以覆盖大更远，所以要删掉）

intervals = [[1,2],[2,3],[3,4],[1,3]]
# intervals = [ [1,2], [1,2], [1,2] ]
# intervals = [ [1,2], [2,3] ]
# intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]

def eraseOverlapIntervals(intervals):
    intervals = sorted(intervals, key = lambda item: item[0])
    remove = 0
    prev = intervals[0]
    for interval in intervals[1:]:
        if interval[0] < prev[1]:
            if interval[1] <= prev[1]:
                prev = interval
            remove += 1
        else:
            prev = interval
    return remove

print(eraseOverlapIntervals(intervals))