#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumber(l1, l2, 0)
    
    def addTwoNumber(self, l1: Optional[ListNode], l2: Optional[ListNode], value) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None if value == 0 else ListNode(1) # 最後有可能進位多一位

        value += l1.val if l1 else 0
        value += l2.val if l2 else 0
        
        digits = value % 10 # 取出個位數
        ten_digits = value // 10 # 取出十位數

        return ListNode(digits, self.addTwoNumber(l1.next if l1 else None, l2.next if l2 else None, ten_digits))


# @lc code=end

