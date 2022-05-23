#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.findLeftMost(root)

    def findLeftMost(self, root):
        while root:
            self.stack.append(root)
            if root.left == None:
                return root
            root = root.left
        return root

    def next(self) -> int:
        node = self.stack.pop()
        self.findLeftMost(node.right)
        return node.val

    def hasNext(self) -> bool:
        return True if self.stack else False

    # def __init__(self, root: Optional[TreeNode]):
    #     self.stack = []
    #     def recursive(node: Optional[TreeNode]) -> None:
    #         '''中序訪問'''
    #         if node == None: 
    #             return

    #         if node.left:   
    #             recursive(node.left)

    #         self.stack.append(node.val)
    #         if node.right:
    #             recursive(node.right)
            
    #     recursive(root)

    # def next(self) -> int:
    #     return self.stack.pop(0)

    # def hasNext(self) -> bool:
    #     return True if self.stack else false


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

