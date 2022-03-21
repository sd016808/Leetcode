#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import Optional
# import math

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Merge Sort O(nlogn)'''
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeSort(left, right)
    
    def mergeSort(self, list1, list2):
        dummy = ListNode(None)
        n = dummy
        while list1 and list2:
            if list1.val < list2.val:
                n.next = list1
                list1 = list1.next
            else:
                n.next = list2
                list2 = list2.next
            n = n.next
        
        if list1:
            n.next = list1
        if list2:
            n.next = list2

        return dummy.next

    def getMid(self, head):
        dummy = ListNode(None, head)
        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        return mid

    def Bublesort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Buble Sort O(n*(n-1)/2) = O(n^2) 的時間複雜度，會TLE'''
        dummy = ListNode(-math.inf, head)
        last = None
        while last != head:
            n = dummy.next
            prev = dummy
            while n != last:
                if prev.val > n.val:
                    n.val, prev.val = prev.val, n.val
                
                prev = n
                n = n.next

            last = prev
        
        return dummy.next

# @lc code=end

