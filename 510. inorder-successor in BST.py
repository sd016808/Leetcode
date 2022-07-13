"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':   
        if not node:
            return None

        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.right == node:
            node = node.parent
        
        return node
        # lastNode = node
        # while node:
        #     if lastNode == node.left:
        #         return node

        #     if node.right and node.right != lastNode:
        #         node = node.right
        #         while node.left:
        #             node = node.left
        #         return node
            
        #     lastNode = node
        #     node = node.parent
        
        # return node