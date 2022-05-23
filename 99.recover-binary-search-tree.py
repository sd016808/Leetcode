#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.stack = []
        def recursive(node):
            if node:
                recursive(node.left)
                self.stack.append(node)
                recursive(node.right)
        
        recursive(root)
        sorted_stack = sorted(self.stack, key=lambda x: x.val)
        for i in range(len(self.stack)):
            if self.stack[i].val != sorted_stack[i].val:
                self.stack[i].val, sorted_stack[i].val = sorted_stack[i].val, self.stack[i].val
                break


# @lc code=end

