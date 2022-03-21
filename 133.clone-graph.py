#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        return self.findNeighbors(node, visited)
    
    def findNeighbors(self, node, visited):
        if node == None:
            return None

        newNode = Node(node.val)
        visited[node.val] = newNode

        for neighbor in node.neighbors:
            if neighbor.val in visited:
                newNode.neighbors.append(visited[neighbor.val])
            else:
                new_neighbor = self.findNeighbors(neighbor, visited)
                if new_neighbor:
                    newNode.neighbors.append(new_neighbor)
            
        return newNode
        
# @lc code=end

