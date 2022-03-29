#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodeCnt = self.getNodeCount(head)
        base = nodeCnt // k
        remain = nodeCnt % k
        group = [base] * k
        group_index = 0
        while remain > 0:
            group[group_index] += 1
            group_index += 1
            remain -= 1

        ans = [None] * k
        for index, num in enumerate(group):
            ans[index] = head
            prev = None
            while num > 0:
                prev = head
                head = head.next
                num -= 1

            if prev:
                prev.next = None

        return ans

    def getNodeCount(self, head):
        cnt = 0
        while head:
            head = head.next
            cnt += 1

        return cnt
# @lc code=end

