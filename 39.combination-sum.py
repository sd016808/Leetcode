#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        candidates.sort()
        def help(offset, count):
            if count == target:
                res.append(stack.copy())
                return
            
            for i in range(offset, len(candidates)):
                # candidates 為 sorted list，若總和已超過 target，後續的loop已無意義
                if count + candidates[i] > target: 
                    break

                stack.append(candidates[i])
                count += candidates[i]
                help(i, count)
                count -= candidates[i]
                stack.pop()
        
        help(0, 0)
        return res
# @lc code=end

