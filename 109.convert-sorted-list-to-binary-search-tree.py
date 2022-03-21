#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None:
            return None

        midNode = self.getMiddleListNode(head)            
        secondHead = midNode.next
        if head == midNode:
            return TreeNode(midNode.val, None, self.sortedListToBST(secondHead))
        else:
            return TreeNode(midNode.val, self.sortedListToBST(head), self.sortedListToBST(secondHead))
    
    def getMiddleListNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        pre = head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        
        pre.next = None
        return slow

# @lc code=end

