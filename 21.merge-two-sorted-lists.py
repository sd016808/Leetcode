#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        n1, n2 = list1, list2
        n = dummy
        while n1 and n2:
            if n1.val < n2.val:
                n.next = n1
                n1 = n1.next 
            else:
                n.next = n2
                n2 = n2.next
            
            n = n.next

        n.next = n2 if n2 else n1
        return dummy.next

# @lc code=end

