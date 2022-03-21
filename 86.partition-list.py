#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        n = head
        pointer1 = dummy1
        pointer2 = dummy2
        while n:
            if n.val < x:
                pointer1.next = n
                pointer1 = n
            else:
                pointer2.next = n
                pointer2 = n

            n = n.next


        pointer1.next = dummy2.next
        pointer2.next = None
        return dummy1.next
    
# @lc code=end

