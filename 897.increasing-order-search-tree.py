#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def in_order_travel(node: TreeNode) -> None:
            if node == None:
                return None

            in_order_travel(node.left)
            self.cur.right = node
            self.cur = self.cur.right
            self.cur.left = None
            in_order_travel(node.right)

        self.dummy = TreeNode(0)
        self.cur = self.dummy
        in_order_travel(root)
        return self.dummy.right
# @lc code=end

