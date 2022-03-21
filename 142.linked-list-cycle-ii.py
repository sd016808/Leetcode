#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Follow up 那個太難，先用 dictionary處理
        visited = set()
        while head:
            if head in visited:
                return head
            else:
                visited.add(head)
                
            head = head.next
        return None
# @lc code=end

