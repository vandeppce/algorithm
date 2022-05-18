# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
#
# 两次反方向遍历，分别贪心
ratings = [1,0,2]
ratings = [1, 2, 2]
ratings = [1, 3, 2, 2, 1]
# ratings = [1,3,4,5,2]
def candy(ratings):
    ret = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            ret[i] = ret[i - 1] + 1
            # ret[i] += 1 # 错误做法

    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            # ret[i] = ret[i + 1] + 1
            if ret[i] <= ret[i + 1]:
                ret[i] = ret[i + 1] + 1
    print(ret)
    return sum(ret)

"""
# 二刷，差不多，反向贪心的时候条件写到一起
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)
"""
print(candy(ratings))