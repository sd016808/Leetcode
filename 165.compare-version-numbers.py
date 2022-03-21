#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_ary = version1.split(".")
        version2_ary = version2.split(".")
        
        return self.compare(version1_ary, version2_ary, 0)

    def compare(self, version1_ary: list, version2_ary: list, offset: int) -> int:
        if offset >= max(len(version1_ary), len(version2_ary)):
            return 0

        v1 = self.tryGet(version1_ary, offset, 0)
        v2 = self.tryGet(version2_ary, offset, 0)

        if v1 > v2:
            return 1
        elif v2 > v1:
            return -1
        else:
            return self.compare(version1_ary, version2_ary, offset + 1)

    
    def tryGet(self, lst: list, index: int, default):
        if index >= len(lst):
            return default
        
        return int(lst[index])


# @lc code=end

