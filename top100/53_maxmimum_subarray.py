from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        f0 = nums[0]
        for i in range(1, n):
            fi = nums[i] + max(0, f0)
            res = max(res, fi)
            f0 = fi
        return res

