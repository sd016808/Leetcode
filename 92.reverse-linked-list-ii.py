#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        n = dummy
        leftTargetParent = None
        cnt = 1

        while cnt != left:
            n = n.next
            cnt += 1
        
        leftTargetParent = n
        while cnt != right + 1:
            n = n.next
            cnt += 1

        start = self.reverse(leftTargetParent.next, n)
        leftTargetParent.next = start

        return dummy.next

    def reverse(self, head, end):
        pre = end.next
        n = head
        while n != end:
            tmp = n.next
            n.next = pre
            pre = n
            n = tmp
        
        end.next = pre
        return end

# @lc code=end

