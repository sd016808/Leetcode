#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#

# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        sort_courses = sorted(courses, key = lambda x: (x[0], x[0] + x[1]))
        ans = 0
        start = 0
        for course in sort_courses:
            end = course[0] + start
            if end <= course[1]:
                start = end
                ans += 1
        
        return ans

[[10,20],[4,13],[4,4],[3,11],[3,5],[3,5]]

# @lc code=end

