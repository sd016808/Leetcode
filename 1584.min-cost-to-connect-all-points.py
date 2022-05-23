#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create edges
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((i, j, math.fabs(points[i][0] - points[j][0]) + math.fabs(points[i][1] - points[j][1])))
        
        # sort edges by distance
        edges.sort(key=itemgetter(2))
        
        # union find
        uf = UnionFind(len(points))
        cost = 0
        for edge in edges:
            i, j, weight = edge
            if uf.connected(i, j):
                continue
        
            uf.union(i, j)
            cost += weight

        return int(cost)

class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.size = {}
        self.count = 1
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1
    
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            # 路徑壓縮
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def union(self, x:int, y: int) -> None:
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root: # already connected
            return

        # 小樹接大樹
        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        self.count -= 1
    



# @lc code=end

