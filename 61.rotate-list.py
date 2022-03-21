#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''先計算總長就知道要將倒數第幾個Node當作Rotate後的頭'''
        if head == None or head.next == None:
            return head

        # 計算總長，為了剔除多餘的循環
        length = 2
        tailNode = head.next
        while tailNode.next:
            length, tailNode = length+1, tailNode.next
        
        # 剔除多餘的循環
        k = k % length
        if k == 0:
            return head
        
        # 將尾巴串回
        tailNode.next = head
        for i in range(0, length - k):
            tailNode = tailNode.next
        
        newHead, tailNode.next  = tailNode.next, None
        return newHead
        # 以下的寫法太笨了，知道總長的情況下要取倒數第 K 個點不需要用到快慢指標，從前面開始數就可以了

        # # 取得倒數第 K 個點
        # slow = head
        # fast = head
        # count = 0
        # while count < k:
        #     fast = fast.next
        #     count += 1
        
        # # 更新倒數第 K 個點為起點
        # preSlow = None # 為了避免 Cyclic 發生
        # lastFast = None # 為了 tail 接回 head
        # while fast:
        #     preSlow = slow
        #     lastFast = fast
        #     slow = slow.next
        #     fast = fast.next

        # preSlow.next = None
        # lastFast.next = head
        #return slow

    def rotateRight_old(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''這個解法不好，理論上知道總長度，就不需要做那麼多次rotate了'''
        if head == None or head.next == None:
            return head

        node = head
        count = 0
        while node != None:
            count += 1
            node = node.next

        k = k % count
        
        return self.rotate(head, k)
    
    
    def rotate(self, head, k):
        if k <= 0:
            return head

        pre = None
        node = head
        while node != None and node.next != None:
            pre = node
            node = node.next
        
        pre.next = None
        node.next = head

        return self.rotate(node, k-1)

# @lc code=end

