#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.stack = []
        def in_order_travel(node: Optional[TreeNode]):
            if node == None:
                return None
            in_order_travel(node.left)
            self.stack.append(node.val)
            in_order_travel(node.right)
        
        in_order_travel(root)
        return self.stack[k-1]

# @lc code=end

