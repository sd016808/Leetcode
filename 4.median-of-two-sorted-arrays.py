#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 目前想不到 O(log (m+n)) 的解法 只能想到 O(m+n) 的解法
        n = len(nums1) + len(nums2)
        merge = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                merge.append(nums1.pop(0))
            else:
                merge.append(nums2.pop(0))
        
        if nums1:
            merge.extend(nums1)
        else:
            merge.extend(nums2)

        if len(merge) & 1 == 0:
            return (merge[n//2] + merge[n//2 - 1]) / 2
        else:
            return merge[n//2]

            
# @lc code=end

