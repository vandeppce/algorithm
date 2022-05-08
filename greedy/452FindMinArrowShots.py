# 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，
# 其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。
#
# 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，
# 若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。
# 可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。
#
# 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
#

points = [[10,16],[2,8],[1,6],[7,12]]
points = [[1,2],[3,4],[5,6],[7,8]]
points = [[1,2],[2,3],[3,4],[4,5]]

def findMinArrowShots(points):
    points = sorted(points, key = lambda x: x[0])
    overlap = [0, 0]
    shots = 0

    for point in points:
        if overlap == [0, 0]:
            overlap = point
            shots += 1
        else:
            if point[0] <= overlap[1]:
                overlap = [max(overlap[0], point[0]), min(overlap[1], point[1])]
            else:
                overlap = point
                shots += 1
    return shots

"""
# 二刷
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda item: item[0])
        num = 1
        interval = points[0]
        for point in points[1:]:
            if point[0] > interval[1]:
                num += 1
                interval = point
            else:
                interval = [max(interval[0], point[0]), min(interval[1], point[1])]
        return num
"""
print(findMinArrowShots(points))