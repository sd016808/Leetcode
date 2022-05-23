#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

from typing import List
import collections

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. build the graph
        graph = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):    
            graph[a][b] = v
            graph[b][a] = 1 / v
        
        # 2. dfs
        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1.0

            if a == b:  
                return 1.0

            for c in graph[a]:
                if c == b:
                    return graph[a][c]
                else:
                    if a == c:
                        continue
                    
                    if c in visited:
                        continue

                    visited.add(c)
                    res = dfs(c, b, visited)
                    visited.remove(c)
                    if res != -1.0:
                        return graph[a][c] * res

            return -1.0
        
        # 3. dfs
        res = []
        for a, b in queries:
            visited = set()
            res.append(dfs(a, b, visited))
        return res

if __name__ == '__main__':
    a = Solution()
    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    print(a.calcEquation(equations, values, queries))
# @lc code=end

