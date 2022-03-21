#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''遞迴的版本'''
        if head == None:
            return head
        
        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head
        
    def removeElements_iterate(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''iterate version'''
        dummy = ListNode(None, head)
        n = head
        prev = dummy
        while n:
            if n.val == val:
                prev.next = n.next
            else:
                prev = n
            
            n = n.next
        return dummy.next
# @lc code=end

