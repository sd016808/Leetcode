#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        for h in range(0, 12):
            for m in range(0, 60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append(str(h) + ':' + str(m).zfill(2))
            
        return res
# @lc code=end

