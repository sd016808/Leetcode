#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''Stack version'''
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        result = None

        while s1 or s2 or carry:
            if s1:
                temp = s1.pop()
                carry += temp
            if s2:
                temp = s2.pop()
                carry += temp

            t = ListNode(carry % 10)
            carry = carry // 10
            t.next = result
            result = t

        return result


# @lc code=end

