#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''遞迴的版本'''
        if head == None or head.next == None:
            return head
       
        dummy = ListNode(None, head)       
        return self.deleteDuplicate(dummy.next, dummy)

    def deleteDuplicate(self, node, prev):
        if node == None:
            return None
        
        if prev.val == node.val or (node.next and node.next.val == node.val):
            return self.deleteDuplicate(node.next, node)
        
        node.next = self.deleteDuplicate(node.next, node)
        return node
            

    def deleteDuplicates_old(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''用loop實作的版本'''
        if head == None or head.next == None:
            return head
       
        dummy = ListNode(0, None)
        prev = dummy
        node = head
        while node:
            tmp = -300
            if node.next and node.val == node.next.val:
                tmp = node.val

            if tmp != -300:
                while node.val == tmp:
                    node = node.next
                    if node == None:
                        prev.next = None
                        break
            else:
                prev.next = node
                prev = node
                node = node.next

        return dummy.next

# @lc code=end

