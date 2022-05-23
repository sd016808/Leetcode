#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

from typing import List

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(curr, k, n) -> int:
            if len(stack) > k:
                return

            if len(stack) == k:
                if sum(stack) == n:
                    res.append(stack[:])
                    return
                else:
                    return
            
            for i in range(curr, 9 + 1):
                if sum(stack) + i > n:
                    break

                stack.append(i)
                backtrack(i + 1, k, n)
                stack.pop()
        
        backtrack(1, k, n)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum3(2, 18))
# @lc code=end

