#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = headA
        n2 = headB
        while n1 != n2:
            n1 = headB if n1 == None else n1.next
            n2 = headA if n2 == None else n2.next
        
        return n1
# @lc code=end

