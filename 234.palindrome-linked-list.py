#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(None, head)
        # 1 2 3 4 slow:2 fast:4  
        # 1 2 3 4 5 slow:3 fast:None
        slow = dummy
        fast = dummy
        pre = None
        while fast and fast.next:
            tmp = slow.next
            slow.next = pre
            slow = tmp
            fast = fast.next.next
        
        head1 = None
        head2 = None
        if fast:
            head1 = slow
        else:
            head1 = slow.next

        slow.next = None
        return slow

# @lc code=end

