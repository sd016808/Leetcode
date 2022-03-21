#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(None, head)
        n = head.next
        dummy.next.next = None
        while n:
            tmp = n.next
            n.next = None
            dummy.next = self.insert(dummy.next, n)
            n = tmp
        
        return dummy.next
    
    def insert(self, head, newNode):
        n = head
        dummy = ListNode(None, head)
        prev = dummy
        while n:
            if n.val >= newNode.val:
                prev.next = newNode
                newNode.next = n
                break

            prev = n
            n = n.next 
        else:
            prev.next = newNode

        return dummy.next
    

Solution().insertionSortList(ListNode(4, ListNode(1,ListNode(2,ListNode(3)))))

# @lc code=end

