from typing import List
from collections import defaultdict

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        hasOne = False
        for i in range(m): # row 
            for j in range(n): # column
                if grid[i][j] == 1:
                    if i > 0 and grid[i - 1][j] == 1:
                        uf.union(i * n + j, (i - 1) * n + j)
                    if j > 0 and grid[i][j - 1] == 1:
                        uf.union(i * n + j, i * n + j - 1)
                    hasOne = True

        if not hasOne:
            return 0
        else:
            return max(uf.size.values())

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
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root: # already connected
            return False

        # 小樹接大樹
        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]

        self.count -= 1
        return True

print(Solution().maxAreaOfIsland([[0]]))