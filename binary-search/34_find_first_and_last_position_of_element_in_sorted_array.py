import bisect
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        ans = [-1, -1]
        
        if n == 0:
            return ans
        lower_bound = bisect.bisect_left(nums, target, lo=0, hi=len(nums))
        if lower_bound >=n or nums[lower_bound] != target:
            return ans
        upper_bound = bisect.bisect_right(nums, target, lo=0, hi=len(nums))
        return [lower_bound, upper_bound - 1] 

print(Solution().searchRange([2, 2], 3))