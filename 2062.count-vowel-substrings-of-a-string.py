#
# @lc app=leetcode id=2062 lang=python3
#
# [2062] Count Vowel Substrings of a String
#

# @lc code=start
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel = ["a", "e", "i", "o", "u"]
        sliding_window = []
        counter = defaultdict(int)
        count = 0
        for c in word:
            if c in vowel:
                sliding_window.append(c)
                counter[c] += 1
            else:
                sliding_window = []
                counter = defaultdict(int)
                continue
            
            left = 0
            tmp = counter.copy()
            while len(tmp.items()) >= 5:
                remove = sliding_window[left]
                tmp[remove] -= 1
                if tmp[remove] <= 0:
                    del tmp[remove]
                
                left += 1
            
            count += left
        
        return count
    

            
# @lc code=end

