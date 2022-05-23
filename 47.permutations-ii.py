#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''利用 Iterator Counter 可以避免重複的組合'''
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results  

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2]))
# @lc code=end

