#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:    
            return
        
        # get middle node to split l1, l2
        l1 = ListNode(0, head)
        l2 = ListNode()
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse l2
        l2.next = slow.next
        l2.next = self.reverse(l2.next)

        # split l1, l2
        slow.next = None
               
        # merge l1, l2
        n1 = l1.next
        n2 = l2.next
        odd = True
        n = ListNode()
        while n1 and n2:
            if odd:
                tmp = n1.next
                n.next = n1
                n = n.next
                n1 = tmp
            else:
                tmp = n2.next
                n.next = n2
                n = n.next
                n2 = tmp
            
            odd = not odd
        
        n.next = n1 if n1 else n2
        return
    
    def reverse(self, head):
        prev = None
        n = head
        while n:
            tmp = n.next
            n.next = prev
            prev = n
            n = tmp
        
        return prev

    def printNode(self, head):
        while head:
            print(head.val)
            head = head.next
# @lc code=end

