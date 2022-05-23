#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''解决该问题的核心是从中心向两端扩散的双指针技巧。'''
        def getPalindrome(s, left, right) -> str:
            '''從left and right 向外推，取得最長的回文字串'''
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right] # 因為最後的left和right會多算一次，所以 left + 1 ，right - 1

        if len(s) <= 1:
            return s
        
        max_palindrome = s[0]
        for i in range(len(s)):
            # 回文為奇數 case: getPalindrome(s, i, i)
            # 回文為偶數 case: getPalindrome(s, i, i+1)
            palindrome = max(getPalindrome(s, i, i), getPalindrome(s, i, i + 1), key=lambda x: len(x))
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome
        
        return max_palindrome
        


# @lc code=end

