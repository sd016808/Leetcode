#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1

            else:
                stack.append([c, 1])

        return "".join([x[0] * x[1] for x in stack])

#print(Solution().removeDuplicates("deeedbbcccbdaa", 3))
# @lc code=end

