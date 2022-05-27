from functools import cache

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s_arr = list(s)
        if len(s_arr) < 2:
            return 0

        stack = []
        offset = 0
        ans = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    offset = i + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        ans = max(ans, i - offset + 1)
                    else:
                        ans = max(ans, i - stack[-1])
        return ans
        # DP 解，麻煩又慢
        # @cache
        # def dp(i: int) -> int:
        #     '''
        #     Returns the longest valid parentheses substring starting at index i
        #     P = i - dp(i-1) - 1
        #     dp(i) = dp(i-2) + 2 if s[i] == ')' and s[i-1] == '('
        #     dp(i) = dp(i-1) + dp(P - 1) + 2 if s[i] == ')' and s[i-1] == ')' and s[P] == '('
        #     dp(i) = 0 if s[i] == '(' or s[P] == ')'
        #     '''
        #     if i < 0 or s_arr[i] == '(' or i - dp(i-1) - 1 < 0:
        #         return 0
        
        #     p = i - dp(i-1) - 1
        #     if s_arr[p] == ')':
        #         return 0

        #     if s_arr[i-1] == '(': # ()
        #         return dp(i-2) + 2
        #     else: # ))
        #         return dp(p-1) + dp(i - 1) + 2
        
        # return max(dp(i) for i in range(len(s)))

if __name__ == "__main__":
    print(Solution().longestValidParentheses(")()())"))
