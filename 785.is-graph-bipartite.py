#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

from typing import List

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = UnionFind(len(graph))
        for i in range(len(graph)): # iterate vertex 
            if not graph[i]:
                continue

            neibors = graph[i]
            for j in range(0, len(neibors)): # iterate vertex's neibors
                if uf.connected(i, neibors[j]):
                    return False

                uf.union(neibors[0], neibors[j])
        return True
            
class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.size = {}
        self.count = n
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
        if x == y:
            return False
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
        
        self.count -= 1
        return True
# @lc code=end

