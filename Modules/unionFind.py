# 用來確保建出來的是Tree不是Graph

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
