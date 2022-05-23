#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

from typing import List

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # create edges
        edges = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i > 0:
                    edges.append(((i - 1, j), (i, j), abs(heights[i - 1][j] - heights[i][j])))
                if j > 0:
                    edges.append(((i, j - 1), (i, j), abs(heights[i][j-1] - heights[i][j])))
        
        # sort edges by weight
        edges.sort(key=lambda x: x[2])

        # union find
        uf = UnionFind(len(heights) * len(heights[0]))
        effort = 0
        for edge in edges:
            point1 = edge[0][1] + edge[0][0] * len(heights[0])
            point2 = edge[1][1] + edge[1][0] * len(heights[0])
            if uf.union(point1, point2):
                effort = max(effort, edge[2])
                if uf.connected(0, len(heights) * len(heights[0]) - 1):
                # 如果當前的集合能夠把起點和終點給連線，此時就是最小的路徑
                    return effort
        return 0

class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.size = {}
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
    
    def union(self, x:int, y: int) -> bool:
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root: # already connected
            return False

        # 小樹接大樹
        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
        elif self.size[x_root] > self.size[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[x_root] = y_root
            self.size[y_root] += 1
        
        return True
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    print(s.minimumEffortPath(heights))