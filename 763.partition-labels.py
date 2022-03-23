#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Segment:
    def __init__(self):
        self.start = None
        self.end = None

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        table = defaultdict(Segment)
        for index, c in enumerate(s):
            if c in table:
                table[c].end = index
            else:
                table[c].start = index
                table[c].end = index

        table = table.values()
        res = [1]
        start = 0
        end = 0
        for x in table:
            if x.start <= end:
                end = max(end, x.end)
                res[-1] = end - start + 1
            else:
                start = x.start
                end = x.end
                res.append(end - start + 1)

        return res

# @lc code=end

