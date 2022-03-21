#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''遞迴的版本'''
        if not head or not head.next:
            return head
        
        head.next = self.deleteDuplicate(head.next, head) 
        return head
    
    def deleteDuplicate(self, node, prev):
        if node == None:
            return None
        
        if prev.val == node.val:
            return self.deleteDuplicate(node.next, node)
        
        node.next = self.deleteDuplicate(node.next, node) 
        return node

    def deleteDuplicates_old(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Loop的版本'''
        dummy = ListNode(-500, head)
        prev = dummy
        node = head
        while node:
            if node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
                
            node = node.next
        
        return dummy.next



# @lc code=end

