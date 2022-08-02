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
        dummy1, dummy2, = ListNode(), ListNode()
        pointer1, pointer2 = dummy1, dummy2
        while head:
            if head.val < x:
                pointer1.next, pointer1 = head, head
            else:
                pointer2.next, pointer2 = head, head

            head = head.next

        pointer1.next, pointer2.next = dummy2.next, None
        return dummy1.next
    
# @lc code=end

