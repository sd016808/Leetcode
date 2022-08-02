# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        
        self.ans=None
        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            if self.ans:
                return
                
            mid = node == p or node == q    
            if mid and left:
                self.ans = node
                return

            right = dfs(node.right)
            if self.ans:
                return

            if (mid and right) or (left and right):
                self.ans = node
                return

            return mid or left or right

        dfs(root)
        return self.ans


