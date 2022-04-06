#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # d = [0] * 300
        # res = 0
        # for i in range(len(arr)):
        #     res += d[target-arr[i]] if target-arr[i] >=0 else 0
        #     res %= (10**9+7)
        #     for j in range(i):
        #         d[arr[i] + arr[j]] += 1

        # return res
        counter = Counter(arr)
        res = 0
        for idx, num in enumerate(arr[:-2]):
            counter[num] -= 1
            tmp = target - num
            copyCounter = counter.copy()
            for num2, count in copyCounter.items():
                if copyCounter[tmp - num2] > 0:
                    if tmp - num2 == num2:
                        res += copyCounter[num2] * (copyCounter[num2] - 1) // 2
                    else:
                        res += copyCounter[tmp - num2] * copyCounter[num2]
                    
                    res %= (10 ** 9 + 7)
                    copyCounter[num2] = 0
                    copyCounter[tmp - num2] = 0
                
        return res               

# if __name__ == '__main__':
#     a = Solution()
#     print(a.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
# @lc code=end

