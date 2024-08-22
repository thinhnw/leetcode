class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [0] * len(nums)
        f[0] = nums[0]
        if len(nums) >= 2:
            f[1] = max(nums[0], nums[1])
        for i in range(2, len(f)):
            f[i] = max(f[i-1], f[i-2] + nums[i])
        return f[-1]