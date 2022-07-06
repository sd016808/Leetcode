#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

from typing import List

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted([w[::-1] for w in set(words)], reverse=True)
        stack = [words[0]]
        for word in words[1:]:
            if stack[-1].startswith(word):
                continue
            else:
                stack.append(word)
        
        ans = 0
        for w in stack:
            ans += len(w) + 1 

        return ans 

# @lc code=end

Solution().minimumLengthEncoding(["abc", "efgabc", "aefgabc"])
