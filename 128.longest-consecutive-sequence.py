#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        uf = UnionFind(nums)
        for n in nums:
            if n - 1 in nums:
                uf.union(n, n - 1)
        
        return uf.maxsize


class UnionFind:
    def __init__(self, nums):
        self.parent = {}
        self.size = {}
        self.maxsize = 1
        for i in nums:
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
            self.maxsize = max(self.maxsize, self.size[y_root])
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.maxsize = max(self.maxsize, self.size[x_root])
        
        return True

print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# @lc code=end

