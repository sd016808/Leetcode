from typing import List
from collections import Counter
from copy import deepcopy

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        counter = Counter(words)
        for word, count in counter.items():
            if self.isMatch(s, word):
                ans += count
    
        return ans
    
    def isMatch(self, s, word):
        i = 0
        for c in word:
            newIndex = s.find(c, i)
            if newIndex == -1:
                return False
            i = newIndex + 1
        return True


print(Solution().numMatchingSubseq("abcde", ["a","bb","acd","ace"]))