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
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        count = 0
        while count != left:
            count += 1
            prev = head
            head = head.next


        return dummy.next

    def reverseLinkList(self, head, end):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head != end:
            n = head.next
            head.next = prev
            prev = head
            head = n

        return end, head


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# @lc code=end

