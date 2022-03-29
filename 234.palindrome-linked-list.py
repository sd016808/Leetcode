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
        if not head or not head.next:
            return head
        dummy = ListNode(None, head)
        # Find 中間點
        # 1 2 3 4 slow:2 fast:4
        # 1 2 3 4 5 slow:3 fast:None
        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 設定第二串的頭
        head2 = slow.next

        # 反轉第一串
        n = dummy.next
        pre = None
        while n != head2:
            tmp = n.next
            n.next = pre
            pre = n
            n = tmp

        # 設定第一串的頭
        head1 = slow if fast else slow.next

        # 檢查兩串是否相同
        while head1 and head2:
            if head1.val != head2.val:
                return False

            head1, head2 = head1.next, head2.next

        return True

# @lc code=end

