#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Recursive Version'''
        if head == None or head.next == None:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseList_iterate(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Iterate Version'''
        prev = None
        n = head
        while n:
            tmp = n.next
            n.next = prev
            prev = n
            n = tmp
        
        return prev
# @lc code=end

