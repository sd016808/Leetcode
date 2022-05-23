#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.list = self._flat(nestedList)
        self.index = 0

    def _flat(self, nestedList: [NestedInteger]):
        lst = []
        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                lst.append(nestedInteger.getInteger())
            else:
                lst.extend(self._flat(nestedInteger.getList()))
        
        return lst
    def next(self) -> int:
        self.index = self.index + 1
        return self.list[self.index - 1]
    
    def hasNext(self) -> bool:
         return self.index < len(self.list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

