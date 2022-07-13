#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
from collections import deque
from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightSideNode = [root.val]
        queue = deque([root])
        while queue:
            count = len(queue)
            for i in range(0, count):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)              
                if node.right:
                    queue.append(node.right)
            
            if queue:
                rightSideNode.append(queue[-1].val)
        
        return rightSideNode

node = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3, right=TreeNode(4)))
print(Solution().rightSideView(node))

# @lc code=end

