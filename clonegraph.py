import copy

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

N_dict = {}
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = []
        if(node==None):
            return None

        # return copy.deepcopy(node)
        return self.DFS(visited,node)

    def DFS(self,visited,node):
        val = node.val
        N_temp = Node(val)
        neighbors = node.neighbors
        N_dict[val]= N_temp
        visited.append(val)
        for neighbor in neighbors:
            if(neighbor.val not in visited):
                N_temp.neighbors.append(self.DFS(visited,neighbor))
            else:
                N_temp.neighbors.append(N_dict[neighbor.val])
        return N_dict[val]

adjList = [[2,4],[1,3],[2,4],[1,3]]
solu = Solution()
ret = solu.cloneGraph(adjList)
print(ret)