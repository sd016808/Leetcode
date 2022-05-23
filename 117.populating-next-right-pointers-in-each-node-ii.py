#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = [root]
        while queue:
            size = len(queue) # 當下level的size
            for i in range(size): # 藉由level的size來判斷是否是最右邊的node
                node = queue.pop(0)
                if i < size - 1: # 如果不是最後一個，就把next指向下一個
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        
# @lc code=end

