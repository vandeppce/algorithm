# 给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。
#
# 所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。
#
# 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
# 假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。
#

class Solution:
    def __init__(self):
        self.res = ["JFK"]

    def backtracking(self, tickets, resLength, begin):
        if len(self.res) == resLength:
            return True

        ends = {}

        for i, item in enumerate(tickets):
            if item[0] == begin:
                ends[item[1]] = i

        if not ends:
            return False

        ends = sorted(ends.items(), key = lambda item: item[0])
        for end in ends:
            self.res.append(end[0])
            begin = end[0]
            _ = tickets.pop(end[1])
            if self.backtracking(tickets, resLength, begin):
                return True
            else:
                self.res.pop()
            tickets.insert(end[1], _)
        # return False # 可加可不加，不加的话递归调用完循环后无返回值，表明为false

    def findItinerary(self, tickets):
        self.backtracking(tickets, len(tickets) + 1, "JFK")
        return self.res

"""
# 二刷，注意这里递归要有返回值
class Solution:
    def __init__(self):
        self.path = ["JFK"]
    
    def 8.backtracking(self, tickets, start):
        if not tickets:
            return True
        
        ends = {}
        for i, item in enumerate(tickets):
            if item[0] == start:
                ends[item[1]] = i
        
        if not ends:
            return False

        ends = sorted(ends.items(), key = lambda item: item[0])

        for end in ends:
            self.path.append(end[0])
            start = end[0]
            ret = tickets.pop(end[1])
            findRes = self.8.backtracking(tickets, start)
            if findRes:
                return True
            else:
                self.path.pop()
                tickets.insert(end[1], ret)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.8.backtracking(tickets, "JFK")
        return self.path
"""
# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
solu = Solution()
print(solu.findItinerary(tickets))