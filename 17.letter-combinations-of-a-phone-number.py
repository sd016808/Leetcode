#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        combination = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(combination, next_digits):
            if len(combination) == len(digits):
                result.append("".join(combination))
                return
            
            for i in range(next_digits, len(digits)):
                for j in mapping[digits[i]]:
                    combination.append(j)
                    backtrack(combination, i + 1)
                    combination.pop()
            
        backtrack(combination, 0)
        return result
# @lc code=end

