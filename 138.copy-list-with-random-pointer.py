#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        n = head
        cache = {}
        while n:
            if not n in cache:
                cache[n] = Node(n.val)

            if n.next:
                cache[n].next = cache.get(n.next, Node(n.next.val))
                cache[n.next] = cache[n].next 
            else:
                cache[n].next = None

            if n.random:
                cache[n].random = cache.get(n.random, Node(n.random.val))
                cache[n.random] = cache[n].random 
            else:
                cache[n].random = None

            n = n.next
        
        return cache[head]

# @lc code=end

