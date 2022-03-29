#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        dummy1 = ListNode(None, head)
        dummy2 = ListNode(None, head.next)
        n1 = dummy1.next
        n2 = dummy2.next
        while n2 and n2.next:
            n1.next = n1.next.next
            n2.next = n2.next.next
            n1 = n1.next
            n2 = n2.next

        n1.next = dummy2.next
        return dummy1.next
# @lc code=end

