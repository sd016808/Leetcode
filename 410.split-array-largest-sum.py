#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        group = [0] * m
        self.ans = 100000000000
        def backtrack(group_offset, nums_offset):
            if nums_offset > len(nums) - 1:
                self.ans = min(self.ans, max(group))
                return

            for g in range(group_offset, m):
                diff = 0
                for i in range(nums_offset, len(nums)):
                    if group[g] >= self.ans:
                        break

                    group[g] += nums[i]
                    backtrack(g + 1, i + 1)
                    diff += nums[i]
                group[g] -= diff
        
        backtrack(0, 0)
        return self.ans

# @lc code=end

