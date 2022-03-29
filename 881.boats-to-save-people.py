#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left= 0
        right = len(people) - 1
        boatsCnt = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1

            boatsCnt += 1

        return boatsCnt


# @lc code=end

